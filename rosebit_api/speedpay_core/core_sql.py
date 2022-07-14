from flask import current_app, session
from rosebit_api.extensions import db



class QuerySpeedPayDB():

    def bind(self):

        self.session = db.session
        session.bind = db.get_engine(current_app, "speedpay")
        return session.bind

    def query_user_phone(self, phone:str):

        session = self.bind()
        data = session.execute(f"SELECT phone_number from users where phone_number='{phone}';")
        serialized_data = [_data for _data in data]
        
        if len(serialized_data) > 0:
            return True
        else:
            return False;

