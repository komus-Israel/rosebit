from flask import Flask
from rosebit_api.api.auth import  auth_router




def create_app(config_name):

    app = Flask(__name__)
    


   

    '''
        @dev    register blueprints
        
    '''

    #   register auth blueprint
    app.register_blueprint(auth_router, url_prefix = "/v1/auth")

    
    return app