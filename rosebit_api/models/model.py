import uuid
from sqlalchemy import UniqueConstraint
from sqlalchemy.dialects.postgresql import UUID
from rosebit_api.extensions import db
import uuid


class Users(db.Model):

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = db.Column(db.String(200), index = True)
    last_name = db.Column(db.String(200), index = True)
    phone = db.Column(db.String(200), index = True)

    def __repr__(self):
        return '<Users %r>' % self.first_name