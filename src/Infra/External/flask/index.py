from flask import Flask, jsonify, request

class FlaskFactory:
    def __init__(self, name=__name__):
        self.app = Flask(name)
        self.configure_app()

    def configure_app(self):
        pass

    def create_app(self):
        return self.app

    @staticmethod
    def request():
        return request

    @staticmethod
    def jsonify(*args, **kwargs):
        return jsonify(*args, **kwargs)
