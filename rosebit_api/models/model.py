from enum import unique
import uuid
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from rosebit_api.extensions import db
import uuid
from sqlalchemy.orm import validates
from datetime import datetime


class User(db.Model):

    __tablename__ = "users"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(200), index = True)
    last_name = db.Column(db.String(200), index = True)
    phone = db.Column(db.String(200), index = True, unique=True)

    @validates("phone_number")
    def validate_contact(self, phone_number):
        if not phone_number.startswith("+") and (
            len(phone_number[1:]) != 13 or len(phone_number[1:]) != 12
        ):
            raise AssertionError("incorrect phone number format")
        return phone_number

    def __repr__(self):
        return '<User %r>' % self.first_name

class UserOTP(db.Model):

    __tablename__ = "user_otp"
    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    otp = db.Column(db.String(6))
    time_sent = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    time_expired = db.Column(db.DateTime)
    phone_number = db.Column(db.String(15), unique=True)

    @validates("phone_number")
    def validate_contact(self, key, phone_number):
        if not phone_number.startswith("+") and (
            len(phone_number[1:]) != 13 or len(phone_number[1:]) != 12
        ):  # noqa: E122
            raise AssertionError("incorrect phone number format")
        return phone_number

    def __repr__(self):
        return f"UserOTP('{self.user_id}','{self.otp}')"