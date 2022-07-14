import requests
from rosebit_api.api_utils.error_logger import logging_error as logger
from threading import Thread
from rosebit_api.api_utils.number_utils import format_phone_no_to_234
import os


USERNAME = os.environ.get('ROUTE_MOBILE_USERNAME')
PASSWORD = os.environ.get('ROUTE_MOBILE_PASSWORD')


def check_balance_on_route_mobile():
    """Check Speedpay's credit balance on ROUTE MOBILE SMS."""
    try:
        BASE_URL = os.environ.get('ROUTE_MOBILE_CHECK_CREDIT_URL')
        url = f'{BASE_URL}username={USERNAME}&password={PASSWORD}'
        response = requests.post(url)
        return response

    except Exception as e:
        logger.error('check_balance_on_route_mobile@Error')
        logger.error(e)
        return None


def process_sms(user_phone_no, body):
    """Send SMS to a user's phone number."""
    try:
        ROUTE_SMS_BASE_URL = os.environ.get('ROUTE_MOBILE_BASE_URL')
        source = 'SpeedPay'
        recipient_no = format_phone_no_to_234(user_phone_no)
        msg = body + " From SpeedpayNG"
        url = f'{ROUTE_SMS_BASE_URL}username={USERNAME}&password={PASSWORD}' \
              f'&type=0&message={msg}&source={source}&destination={recipient_no}&dlr=1'
        response = requests.post(url)
        return response
    except Exception as e:
        logger.error('async_sms@Error')
        logger.error(e)
        return None


def send_sms(phone_number, body):
    """Execute async_sms asynchronously using Thread."""
    try:
        thr = Thread(target=process_sms, args=[phone_number, body])
        thr.start()
        return thr
    except Exception as e:
        logger.error('send_sms@Error')
        logger.error(e)
        return None
