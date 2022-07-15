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

    SQLALCHEMY_DATABASE_URI = "postgres://cmajacmlqoaurn:b9facb78f0b32f683dc3cc883e9a17b0bb48c7fcc8e3604ed5a5286baf28a832@ec2-54-228-32-29.eu-west-1.compute.amazonaws.com:5432/dctnjsd3q1ramk"#os.getenv('DATABASE_URL')
    SQLALCHEMY_BINDS = {

                           # "speedpay": "postgresql://posgres:123@localhost:5453/speedway"
                           "speedpay":  "postgresql://jmmtnbyuosjoxa:14e2ae695b354b0e2f6fb1bda3606647f581f6ad91f2785d34c6764acd8718e6@ec2-52-207-74-100.compute-1.amazonaws.com:5432/d4601mjn96c8u1" #os.environ.get("SPEEDPAY_TEST_DB")

                        }
    
    #if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    #    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)
    
    

config = {
    'development':DevelopmentConfig,
    'production':ProductionConfig,
    'default':DevelopmentConfig,
    'test':TestConfig,
    'staging': StagingConfig
}