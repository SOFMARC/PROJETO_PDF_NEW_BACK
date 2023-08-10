import os
from functools import wraps
from datetime import date
from src.Interface.Api.utils.config import path
from datetime import datetime, timedelta
from src.Interface.Api.utils.clear import clear_folder_upload
from src.Interface.Api.works.work_controller import work_controller
from src.Infra.External.jwt.index import JwtFactory
from src.Infra.External.pyodbc.index import Database
from src.Infra.External.flask.index import FlaskFactory
from src.Infra.External.werkzeug.index import WerkzeugFactory
from src.Infra.External.flask_cors.index import FlaskCorsFactory
from src.Infra.Database.UserDatabaseRepository import UserRepositoryInfra
from src.Interface.Api.celery_worker import celery, process_pdf


factory = FlaskFactory()
app = factory.create_app()

UPLOAD_FOLDER = ''+path+'Api/uploads'

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['SECRET_KEY'] = '$$JUju5040'

cors = FlaskCorsFactory.CORS(app)

db = Database()
db_user = UserRepositoryInfra(db)

app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/0',
    CELERY_RESULT_BACKEND='redis://localhost:6379/0'
)

celery.conf.update(app.config)

def get_date_format():
    # Data original
    data = date.today()


    # Formatação da data
    data_formatada = data.strftime("%a, %d %b %Y %H:%M:%S GMT")

    return data_formatada

def gerar_token(usuario):
    
    payload = {
        'sub': usuario[0][2],
        'exp': datetime.utcnow() + timedelta(minutes=600)
    }
    
    token = JwtFactory.jwt().encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token


def gerar_token_login(usuario):

    payload = {
        'sub': usuario[0][4],
        'exp': datetime.utcnow() + timedelta(minutes=600)
    }
    
    token = JwtFactory.jwt().encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def gerar_token_cadastro(usuario):
    
    payload = {
        'sub': usuario,
        'exp': datetime.utcnow() + timedelta(minutes=600)
    }
    
    token = JwtFactory.jwt().encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return token

def autenticar(rota):
    @wraps(rota)
    def wrapper(*args, **kwargs):
        token = factory.request().headers.get('Authorization')
        
        if not token:
            return {'mensagem': 'Token ausente'}, 401
        try:
            payload = JwtFactory.jwt().decode(token.split()[1], app.config['SECRET_KEY'], algorithms=['HS256'])
            
            if payload['sub']:
                
                try:

                    db = Database() 
                
                    db.connect()

                    res = db.get_user_v2(payload['sub'])
                    

                    usuario = res, 200
            
                finally:

                    db.close()
            
        except (JwtFactory.DecodeError(), JwtFactory.ExpiredSignatureError()):
            return {'mensagem': 'Token inválido ou expirado'}, 401
        if usuario == []:
            return {'mensagem': 'Usuário não encontrado'}, 401
        return rota(usuario, *args, **kwargs)
    
    return wrapper

@app.route("/")
def index():
    return factory.jsonify( name="pdfreaderui", status="active", version= "0.0.1")


@app.route('/uploader', methods = ['POST'])
@autenticar
def upload_file(usuario):
    if usuario:
        f = factory.request().files['file']
        filename = WerkzeugFactory.secure_filename(f.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        filepathimage = os.path.join(app.config['UPLOAD_FOLDER']+'/image_pdf/', filename.replace('.pdf', '.jpg'))

        f.save(filepath)

        db = Database() 


        task = process_pdf.delay(filepath, filename, filepathimage, usuario[0][0])

        db.connect()

        res = db.insert_uploads(usuario[0][0], date.today(), filename, 1, 1, task.id)

        db.close()

        return factory.jsonify( upload_id=res, data=get_date_format(), nome=filename, task_id=task.id, status_task="Em andamento", status=200)

    else:
        return factory.jsonify( status="not authentication",  res = 400)

    
        # # Faz uma solicitação para o endpoint do Celery que processa o PDF
        # response = requests.post('http://127.0.0.1:6000' + '/process_pdf', data={'file_path': filepath})
        
        # if response.status_code == 202:
        #     task_id = response.json().get('task_id')
        #     return factory.jsonify({'task_id': task_id}), 202
        # else:
        #     return factory.jsonify({'error': 'Failed to process PDF'}), 500

        #task = process_pdf.delay(filepath)

        #return factory.jsonify({'task_id': task.id}), 202
        
"""         try : 
            res = work_controller(filepath, filename, filepathimage)
            clear_folder_upload(filepath)

        except:
            return factory.jsonify( name="error to processing the pdf",  status=400)
            
        if res == 200:
        
                return factory.jsonify( name="upload success", status=200 )
        else:
                return factory.jsonify( name="error to processing the pdf",  status=400) """
    
@app.route('/auth', methods = ['GET'])
@autenticar
def auth(usuario):
    if usuario:
        if usuario[0]!= []:
            try:
                return factory.jsonify( status="success authentication", id=usuario[0][0], name=usuario[0][1], email=usuario[0][2], id_perfil=usuario[0][3], id_client=usuario[0][4], empresa=usuario[0][5],  res = 200 )
            finally:
                print("entrei")
        else:
            return factory.jsonify( status="not authentication",  res = 400)
    

@app.route('/user/uploads', methods = ['GET'])
@autenticar
def user_uploads(usuario):
    if usuario:
        if usuario[0]!= []:
            try:
                
                db = Database() 
                db.connect()
                
                try:
                    res = db.get_user_upload(usuario[0][0]) #(usuario[0][0]

                    users = [{'upload_id': row[0], 'data': row[2], 'nome': row[3], 'status_upload': row[4], 'task_id': row[6], 'status_task':row[8]} for row in res]

                    db.close()

                    if res == []:

                        return factory.jsonify( status="uploads empy",  res = 200 )
                    else:
                        #return factory.jsonify( upload_id=res[0][0], data=res[0][2],nome=res[0][3], status_upload=res[0][4], task_id=res[0][6], status_task=res[0][8],  res = 200 )
                        return factory.jsonify(uploads=users)
                finally:
                    print("fim update")
            finally:
                print("fim")
        else:
            return factory.jsonify( status="not authentication",  res = 400)
    else:
        return factory.jsonify( status="not authentication",  res = 400)



@app.route('/user/relatoio', methods = ['GET'])
@autenticar
def user_relatorio(usuario):
    if usuario:
        if usuario[0]!= []:
            try:
                db = Database() 
                db.connect()
                
                try:
                    res = db.relatorio(usuario[0][4])
                    
                    print("###############################RELATÓRIO###############################")
                    print(usuario[0][4])

                    users = [{'razao_prestador': row[0], 'cnpj_prestador': row[1], 'nim_nota_fiscal': row[2], 'codigo_servico': row[3], 'mun_emissao': row[4], 'mun_prestacao':row[5], 'valor_total_nota':row[6], 'base_de_calculo':row[7], 'aliquota':row[8], 'valor_iss':row[9], 'status':row[10]} for row in res]

                    db.close()

                    if res == []:

                        return factory.jsonify( status="uploads empy",  res = 200 )
                    else:
                        #return factory.jsonify( upload_id=res[0][0], data=res[0][2],nome=res[0][3], status_upload=res[0][4], task_id=res[0][6], status_task=res[0][8],  res = 200 )
                        return factory.jsonify(relatorio=users)
                finally:
                    print("fim update")
            finally:
                print("fim")
        else:
            return factory.jsonify( status="not authentication",  res = 400)
    else:
        return factory.jsonify( status="not authentication",  res = 400)




@app.route('/user/all', methods = ['GET'])
@autenticar
def user_uploads_all(usuario):
    if usuario:
        if usuario[0]!= []:
            try:
                try:

                    db = Database() 
                    db.connect()

                    res = db.check_users_inseridos(usuario[0][4])

                    print("usuario", res)
                
                    users = [{'id': row[0], 'name': row[1], 'email': row[2]} for row in res]

                    db.close()

                    return factory.jsonify(data=users)

                finally:
                    print("cadastro")

            finally:            
                print("nao informado")
                

        else:
            return factory.jsonify( status="not authentication",  res = 400)
    else:
        return factory.jsonify( status="not authentication",  res = 400)

@app.route('/logs/upload/<upload_id>', methods = ['GET'])
def user_uploads_logs(upload_id):
    if upload_id:

            try:

                try:

                    db = Database() 
                    db.connect()

                    res = db.get_logs_uploads(upload_id)

                    users = [{'id': row[0], 'data': row[2], 'log': row[3]} for row in res]

                    db.close()

                    return factory.jsonify(logs=users)

                finally:
                    print("cadastro")

            finally:            
                print("nao informado")

    else:
        return factory.jsonify( status="not authentication",  res = 400)

@app.route('/cadastro', methods = ['POST'])
def cadatro_user():
    try:

        senha_criptografada = WerkzeugFactory.generate_password_hash(factory.request().json.get("password", None))

        db = Database() 

        db.connect()
        id_cliente = db.insert_client(factory.request().json.get("empresa", None))


        #id_perfil = db.insert_tab_perfil(factory.request().json.get("name", None), 1, date.today(), 'sim')

        id = db.insert_usuarios(id_cliente, 183, factory.request().json.get("name", None), factory.request().json.get("email", None), senha_criptografada)
        db.close()

        # db.connect()
        # db_user.save(factory.request().json.get("name", None), factory.request().json.get("email", None), senha_criptografada)
        # db.close()

        if id:
            token = gerar_token_cadastro(factory.request().json.get("email", None))

            #print(token)
            
            return factory.jsonify( email=factory.request().json.get("email", None),token=token , status=200)
        else:
            return factory.jsonify( name="error",  status=400)
    except:
        return factory.jsonify( name="error",  status=400)

@app.route('/cadastro/permission', methods = ['POST'])
def cadatro_user_permission():
    try:

        senha_criptografada = WerkzeugFactory.generate_password_hash(factory.request().json.get("password", None))

        db = Database() 

        db.connect()
        
        id = db.insert_usuarios(factory.request().json.get("id_cliente", None), factory.request().json.get("per_id", None), factory.request().json.get("name", None), factory.request().json.get("email", None), senha_criptografada)
        
        db.close() 

        if id:
            return factory.jsonify( id=id, id_cliente=factory.request().json.get("id_cliente", None), per_id=factory.request().json.get("per_id", None), name=factory.request().json.get("name", None), email=factory.request().json.get("email", None), status=200)
        else:
            return factory.jsonify( name="error",  status=400)
    except:
        return factory.jsonify( name="error",  status=400)

@app.route('/delete/permission', methods = ['DELETE'])
def delete_user_permission():
    try:

        db = Database() 

        db.connect()
        
        db.delete_users(10)

        db.close()


        return factory.jsonify( name="delete sucess", status=200)
    
    except:

        return factory.jsonify( name="error",  status=400)



@app.route('/login', methods = ['POST'])
def login_user():
        
        db = Database() 

        db.connect()
        res = db.check_user_login(factory.request().json.get("email", None), factory.request().json.get("password", None))

        
        password = res[0][5] if res !=[] else []

        db.close()
        
        if res != [] and WerkzeugFactory.check_password_hash(password, factory.request().json.get("password", None)):
            
            token = gerar_token_login(res)
        
            #print(token)
            return factory.jsonify( email=factory.request().json.get("email", None), token=token, status=200)
        else :
            return factory.jsonify( name="error",  status=400)

##processamento em fila dos arquivos
@app.route('/task_status/<task_id>')
def task_status(task_id):
    task = process_pdf.AsyncResult(task_id)

    if task.state == 'PENDING':
        response = {
            'status': 'waiting',
            'message': 'Task is waiting to be processed'
        }
    elif task.state == 'STARTED':
        response = {
            'status': 'processing',
            'message': 'Task is currently being processed'
        }
    elif task.state == 'SUCCESS':
        response = {
            'status': 'completed',
            'message': 'Task has been processed successfully',
            'result': task.result
        }
    else:
        response = {
            'status': 'failed',
            'message': 'Task failed to process'
        }

    return factory.jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
