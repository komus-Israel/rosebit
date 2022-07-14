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
        db.session.commit(user_otp)
        otp = user_otp.otp
        return otp
    except Exception as e:
        db.session.rollback()
        logger.error('generate_otp@Error')
        logger.error(e)
        return None

