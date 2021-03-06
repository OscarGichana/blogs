import os
from flask_simplemde import SimpleMDE

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://oscar:123@localhost/blog"
    SECRET_KEY = os.environ.get('SECRET_KEY')
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
 
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://oscar:123@localhost/blog"
    DEBUG = True

class TestConfig(Config):
    pass

class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://oscar:123@localhost/blog"
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}