from random import random
from datetime import datetime, timedelta
from rosebit_api.extensions import db 
from rosebit_api.models.model import UserOTP
from rosebit_api.api_utils.error_logger import logging_error as logger


def timed_random_gen():
    '''
    OTP as global variable only changes value once the application
    restarts otherwise it remains the same
    '''
    
    OTP = str(random())[2:8]  # Generate random numbers for OTP
    EXPIRY_TIME = datetime.now() + timedelta(minutes=7)  # Reset expiry time for new OTP
    return OTP, EXPIRY_TIME


def generate_otp(phone_number):
    """Create new UserOTP for this phone number."""
    try:
        OTP, EXPIRY_TIME = timed_random_gen()
        user_otp = UserOTP(
            otp=OTP,
            time_expired=EXPIRY_TIME,
            phone_number=phone_number
        )

        db.session.add(user_otp)
        db.session.commit()
        return OTP
        
    except Exception as e:
        db.session.rollback()
        logger.error('generate_otp@Error')
        logger.error(e)
        return None

def get_otp_by_phone_number(phone_number):
    """Retrieve UserOTP by phone number."""
    try:
        return UserOTP.query.filter_by(phone_number=phone_number).first()
    except Exception as e:
        logger.error('get_otp_by_phone_number@Error')
        logger.error(e)
        return None


def update_otp(user_otp):
    """Update UserOTP otp and time_expired fields."""
    try:
        # An instance of UserOTP must be passed as parameter not a phone_numer,
        # inorder to update its otp and time_expired fields
        # user_otp = get_otp_by_phone_number(phone_number)
        OTP, EXPIRY_TIME = timed_random_gen()
        user_otp.otp = OTP
        print(OTP)
        user_otp.time_expired = EXPIRY_TIME
        db.session.commit() # the otp returned is not commited to db
        otp = user_otp.otp
        print(otp)
        return otp
    except Exception as e:
        db.session.rollback()
        logger.error('update_otp@Error')
        logger.error(e)
        return None


