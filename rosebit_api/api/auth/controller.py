from flask import request
from rosebit_api.api.auth import auth_router
from rosebit_api.extensions import db
from rosebit_api.api.auth.services import *






@auth_router.post("/onboarding/step-one")
def step_one_onboarding():

    #   return the step one onboarding process service
    return OnboardingService.step_one_onboarding(request.json)

@auth_router.post("/onboarding/verify/phone")
def verify_phone():
    return OnboardingService.verify_phone_number(request.json)

@auth_router.post("/onboarding/email/send")
def send_email_verification():
    return OnboardingService.send_email_verification(request.json)

@auth_router.post("onboarding/verify/email")
def step_two_onboarding():
    return OnboardingService.step_two_onboarding(request.json)




    