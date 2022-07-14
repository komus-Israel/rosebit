from flask import current_app, jsonify
from rosebit_api.api.auth import auth_router
from rosebit_api.extensions import db
from rosebit_api.api.auth.services import *






@auth_router.get("/test/<string:number>")
def get_test(number):

    OnboardingService.step_one_onboarding(number)
    return jsonify(status="working")