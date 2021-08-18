import os


class Config:
    '''
    General configuration parent class
    '''
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://waichinga:MainaMuiri@localhost/pitch'
    UPLOADED_PHOTOS_DEST ='app/static/photos'
    
     # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True




class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://waichinga:MainaMuiri@localhost/pitch_test'


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgres://aiyehkyasqnfou:7492be85e875ff99a6a644c439a1431ba11f85592390b41abddd94c47551bb85@ec2-44-196-170-156.compute-1.amazonaws.com:5432/dbjhv29qe54hen'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}