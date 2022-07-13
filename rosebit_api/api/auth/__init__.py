from flask import Blueprint

auth_router = Blueprint("auth", __name__)


#   import the routes in the controller
from rosebit_api.api.auth.controller import *