import os


basedir = os.path.abspath(os.path.dirname(__file__))


class Config:

    JWT_SECRET_KEY =  os.environ.get("JWT_SECRET_KEY")
    #JWT_ACCESS_TOKEN_EXPIRES = True
    

    @staticmethod
    def init_app(app):
        pass



class DevelopmentConfig(Config):

    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  os.environ.get("SQLALCHEMY_DATABASE_DEV_URI") #"postgresql://posgres:123@localhost:5455/rosebit" #
    SQLALCHEMY_BINDS = {

                           # "speedpay": "postgresql://posgres:123@localhost:5453/speedway"
                           "speedpay": os.environ.get("SPEEDPAY_TEST_DB")

                        }
    
class ProductionConfig(Config):

    DEBUG = True

class TestConfig(Config):

    
    DEBUG = True
    SQLALCHEMY_DATABASE_URI =  os.environ.get("SQLALCHEMY_DATABASE_TEST_URI")
    
    

class StagingConfig(Config):

    DEBUG = True

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    
    if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    
    

config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig,
    'test':TestConfig,
    'staging': StagingConfig
}