import os
DATABASE_URI='postgresql+psycopg2://moringa:123456#$@localhost/abdiaziz3'
class Config:

    '''
    General configuration parent class
    '''
    SECRET_KEY = 'powerfulsecretkey'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True
    


class ProdConfig(Config):
    '''
    Pruduction configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")

class TestConfig(Config):
    '''
    Testing configuration child class

    Args:
        Config: The parent configuration class with General configuration settings 
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration child class
    
    Args:
        Config: The parent configuration class with General configuration settings
    '''
  
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URI")
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig,
    'test': TestConfig
}