from rosebit_api.speedpay_core.core_sql import QuerySpeedPayDB
from flask import jsonify

speedPayDB = QuerySpeedPayDB()

class OnboardingService():

    def step_one_onboarding(phone):
        
        status, speedpayOnboardingData = speedPayDB.query_user_details_by_phone(phone)
        
        if (status == True):

            return jsonify(

                status = "success",
                message = "number existing on speedpay",
                speedpayOnboarding = status,
                data = speedpayOnboardingData,

            ), 200
        

        


    def step_two_onboarding(self):
        pass 

    def step_three_onboarding(self):
        pass


class AuthService():

    def login():
        pass 
    
