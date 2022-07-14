#from rosebit_api.api import create_app
from rosebit_api.api_utils.error_logger import logging_error as logger
import os
from mailjet_rest import Client as MailClient
from threading import Thread


#app = create_app("development")

API_KEY = os.environ.get("MAILJET_API_KEY")
API_SECRET = os.environ.get("MAILJET_SECRET")

# Default Speedpay Mail
DEFAULT_MAILER = os.environ.get("DEFAULT_MAILER")


def process_email(user, email, subject: str, body: str):
    """
    Send EMAIL.
    :param user: an instance of User model
    :param subject: subject of the mail
    :param body: body of the mail
    :return:
    """
    try:
        #with app.app_context():
            # Authentication using API KEY and API SECRET.
        mailer = MailClient(auth=(API_KEY, API_SECRET), version="v3.1")
        fullname = user.first_name + " " + user.last_name
        data = {
            "Messages": [
                {
                    "From": {
                        "Email": DEFAULT_MAILER,
                        "Name": "Rosebit"
                    },
                    "To": [{
                        "Email": email,
                        "Name": fullname
                    }],
                    "Subject": subject,
                    "HTMLPart": f"""<h4>Dear {fullname}</h4> {body}""",
                }
            ]
        }
        response = mailer.send.create(data=data)
        return response
    except Exception as e:
        print(e)
        logger.error('async_email@Error')
        logger.error(e)
        return None


def send_email(user, email, subject: str, body: str):
    """
    Execute process_email asynchronously using Thread.
    :param user: Instance = user instance must be passed not user.id
    :param subject: str = subject of the mail to be sent
    :param body: str = body of the mail to be sent
    :return: a Thread which sends the mail to the user
    """
    try:
        thr = Thread(target=process_email, args=[user, email, subject, body])
        thr.start()
        return thr
    except Exception as e:
        logger.error('send_email@Error')
        logger.error(e)
        return None
