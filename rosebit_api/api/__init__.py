from flask import Flask
from rosebit_api.api.auth import  auth_router
from rosebit_api.config import config
from rosebit_api.extensions import db




def create_app(config_name):

    app = Flask(__name__)
    

    """ app configuration setup """
    app.config.from_object(config.config[config_name])


    """ intialization of dependencies """

    db.init_app(app)        #   db initialization with the app

   

    '''
        @dev    register blueprints
        
    '''

    #   register auth blueprint
    app.register_blueprint(auth_router, url_prefix = "/v1/auth")

    
    return app