from flask import Flask, request,  jsonify
from werkzeug.utils import secure_filename
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
from PIL import Image
import os
from works.work_controller import work_controller
from flask_cors import CORS
from utils.clear import clear_folder_upload
from utils.config import path
from provider.database import Database
from functools import wraps
from jwt.exceptions import DecodeError, ExpiredSignatureError
from datetime import datetime, timedelta

application = Flask(__name__)
app=application

UPLOAD_FOLDER = ''+path+'/api/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = '$$JUju5040'

cors = CORS(app)
db = Database()

def gerar_token(usuario):
    
    payload = {
        'sub': usuario[0][2],
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def gerar_token_cadastro(usuario):
    
    payload = {
        'sub': usuario,
        'exp': datetime.utcnow() + timedelta(minutes=30)
    }
    
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def autenticar(rota):
    @wraps(rota)
    def wrapper(*args, **kwargs):
        token = request.headers.get('Authorization')
        if not token:
            return {'mensagem': 'Token ausente'}, 401
        try:
            payload = jwt.decode(token.split()[1], app.config['SECRET_KEY'], algorithms=['HS256'])
            db.connect()
            res = db.get_user(payload['sub'])
            db.close()
            usuario = res
        except (DecodeError, ExpiredSignatureError):
            return {'mensagem': 'Token inválido ou expirado'}, 401
        if usuario == []:
            return {'mensagem': 'Usuário não encontrado'}, 401
        return rota(usuario, *args, **kwargs)

    return wrapper


@app.route("/")
def index():
    return jsonify( name="pdfreaderui", status="active", version= "0.0.1")

@app.route('/uploader', methods = ['POST'])
@autenticar
def upload_file(usuario):
    if usuario:
        f = request.files['file']
        filename = secure_filename(f.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        filepathimage = os.path.join(app.config['UPLOAD_FOLDER']+'/image_pdf/', filename.replace('.pdf', '.jpg'))

        f.save(filepath)
        
        try : 
            res = work_controller(filepath, filename, filepathimage)
            clear_folder_upload(filepath)

        except:
            return jsonify( name="error to processing the pdf",  status=400)
            
        if res == 200:
        
                return jsonify( name="upload success", status=200 )
        else:
                return jsonify( name="error to processing the pdf",  status=400)
    
@app.route('/auth', methods = ['POST'])
@autenticar
def auth(usuario):
    if usuario:
        return jsonify( name="success authentication", status = 200 )
    else:
        return jsonify( name="not authentication",  status = 400)


@app.route('/cadastro', methods = ['POST'])
def cadatro_user():
    try:
        db.connect()

        senha_criptografada = generate_password_hash(request.json.get("password", None))
        
        db.insert_data(request.json.get("name", None), request.json.get("email", None), senha_criptografada)
            
        db.close()

        token = gerar_token_cadastro(request.json.get("email", None))

        print(token)
        
        return jsonify( email=request.json.get("email", None),token=token , status=200)
    except:
        return jsonify( name="error",  status=400)
    
@app.route('/login', methods = ['POST'])
def login_user():
        db.connect()
        
        res = db.check_user_login(request.json.get("email", None), request.json.get("password", None))
        
        print(res)

        db.close()
        
        password = res[0][3] if res !=[] else []
        
        print(password)

        print(check_password_hash(request.json.get("password", None), password))

        if res != [] and check_password_hash(password, request.json.get("password", None)):
            token = gerar_token(res)

            print(token)
            return jsonify( email=request.json.get("email", None), token=token, status=200)
        else :
            return jsonify( name="error",  status=400)
        

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
