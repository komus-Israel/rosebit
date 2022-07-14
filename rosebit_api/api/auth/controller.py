from flask import current_app, jsonify
from rosebit_api.api.auth import auth_router
from rosebit_api.extensions import db





@auth_router.get("/test/<string:number>")
def get_test(number):

    #number_exist = speedPayDB.query_user_phone(number)
    return jsonify(status="working", msg=number_exist)