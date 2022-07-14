from datetime import datetime
from os import access
from rosebit_api.speedpay_core.core_sql import QuerySpeedPayDB
from flask import jsonify, g 
from rosebit_api.models.model import User
from rosebit_api.extensions import db, jwt
from rosebit_api.otp.crud import generate_otp, get_otp_by_phone_number, update_otp
from rosebit_api.sms.base import send_sms
from rosebit_api.email.base import send_email
from flask_jwt_extended import create_access_token

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
        
        fetch_number_from_rosebit = User.query.filter_by(phone_number = data["phone"]).first()

        if not fetch_number_from_rosebit:

            step_one_onboarding = User(

                first_name  = data["first_name"],
                last_name = data["last_name"]
            )

            db.session.add(step_one_onboarding)
            db.session.commit()
            
            otp = generate_otp(data["phone"])

            if not otp:

                return jsonify(msg="otp sent"), 403

            send_sms(data["phone"], f"Your Rosebit verification code is {otp}")

            return jsonify(

                status = "success",
                msg = "check your sms for verification the verification code",
                speedpayOnboarding = False,
                id = step_one_onboarding.id
            ), 201

        

    def verify_phone_number(data):

        submitted_otp = data["otp"]
        phone_number = data["phone_number"]
        user_id = data["id"]

        generated_otp = get_otp_by_phone_number(phone_number)

        if datetime.utcnow() > generated_otp.time_expired :

            return jsonify(

                status = "failed",
                msg = "expired otp",
            ), 403
       

        if not generated_otp.otp:
    
            return jsonify(

                status = "failed",
                msg = "invalid otpp",
            ), 400

        if generated_otp.otp != submitted_otp:
            return jsonify(

                status = "failed",
                msg = "invalid otp",
            ), 400

        get_user = User.query.get_or_404(user_id)

        get_user.phone_number = phone_number
        get_user.phone_number_verified = True
        db.session.commit()

        return jsonify (

            status = "success",
            msg = "number verified"
        )

    #   send verification link to email
    def send_email_verification(data):

        user_otp = get_otp_by_phone_number(data["phone_number"])
        user = User.query.filter_by(phone_number = data["phone_number"]).first()

        if not user_otp:
            return jsonify(
                msg = "phone number not verified",
                status = "failed"
            ), 401
        
        updated_otp = update_otp(user_otp)
        send_email(user, data["email"], "Email Verification", f"Your Rosebit email verification code is {updated_otp}")
        return jsonify(

            msg = "check email for verification code",
            status = "success",


        ), 201
       

    def step_two_onboarding(data):
        
        submitted_otp = data["otp"]
        phone_number = data["phone_number"]
        user_email = data["email"]
        user_id = data["id"]

        generated_otp = get_otp_by_phone_number(phone_number)

        if datetime.utcnow() > generated_otp.time_expired :
    
            return jsonify(

                status = "failed",
                msg = "expired otp",
            ), 403

        if not generated_otp.otp:
    
            return jsonify(

                status = "failed",
                msg = "invalid otpp",
            ), 400

        if generated_otp.otp != submitted_otp:
            return jsonify(

                status = "failed",
                msg = "invalid otp",
            ), 400
        
        get_user = User.query.get_or_404(user_id)

        get_user.email = user_email
        get_user.email_verified = True
        db.session.commit()

        g.user = get_user
        access_token = create_access_token(identity=g.user.email)

        return jsonify (

            status = "success",
            msg = "email verified",
            id = user_id,
            access_token = access_token,
            data =  dict(
                email_verified = get_user.email_verified,
                phone_verified = get_user.phone_number_verified
            )
        )





class AuthService():

    def login():
        pass 
    
