from flask_cors import CORS

class FlaskCorsFactory:
    
    @staticmethod
    def CORS(app):
        return CORS(app)

