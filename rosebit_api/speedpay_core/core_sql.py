from flask import current_app, session
from rosebit_api.extensions import db



class QuerySpeedPayDB():

    """ set up the bind session to be used to execute queries """

    def bind(self):

        self.session = db.session
        session.bind = db.get_engine(current_app, "speedpay")
        return session.bind

    """ check if number has been registered in speedpay """
    
    def query_user_details_by_phone(self, phone:str):

        session = self.bind()
        data = session.execute(f"SELECT phone_number, phone_number_verified, email_verified, kyc_completed from users where phone_number='{phone}';")
        serialized_data = [_data for _data in data]
        phone_number, phone_number_verified, email_verified, kyc_completed = serialized_data[0]
        
        if len(serialized_data) > 0:

            return True, dict(
                    phone_number = phone_number, phone_number_verified = phone_number_verified, 
                    email_verified = email_verified, kyc_completed = kyc_completed
                    )

        else:

            return False, {}

