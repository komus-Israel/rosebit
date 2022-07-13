from flask import jsonify
from rosebit_api.api.auth import auth_router

@auth_router.get("/test")
def get_test():
    return jsonify(status="working")