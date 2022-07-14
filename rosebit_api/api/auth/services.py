from rosebit_api.speedpay_core.core_sql import QuerySpeedPayDB
from flask import jsonify
from rosebit_api.models.model import User
from rosebit_api.extensions import db

speedPayDB = QuerySpeedPayDB()

class OnboardingService():

    def step_one_onboarding(data):
        
        status, speedpayOnboardingData = speedPayDB.query_user_details_by_phone(data["phone"])
        
        if (status == True):

            return jsonify(

                status = "success",
                msg = "number existing on speedpay",
                speedpayOnboarding = status,
                data = speedpayOnboardingData,

            ), 200
        
        fetch_number_from_rosebit = User.query.filter_by(phone = data["phone"]).first()

        if not fetch_number_from_rosebit:

            step_one_onboarding = User(

                first_name  = data["first_name"],
                last_name = data["last_name"]
            )

            db.session.add(step_one_onboarding)
            db.session.commit()
            
            return jsonify(

                status = "success",
                msg = "check sms for verification",
                id = step_one_onboarding.id
            )

        


    def step_two_onboarding(self):
        pass 

    def step_three_onboarding(self):
        pass


class AuthService():

    def login():
        pass 
    
