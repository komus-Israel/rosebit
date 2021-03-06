from rosebit_api.api import create_app
from rosebit_api.extensions import db
from rosebit_api.models.model import User, UserOTP

app = create_app("staging")





#   configure shell feature to query database from shell

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User, UserOTP = UserOTP)

with app.app_context():
    db.create_all()
