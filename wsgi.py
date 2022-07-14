from rosebit_api.api import create_app
from rosebit_api.extensions import db
from rosebit_api.models.model import User

app = create_app("development")





#   configure shell feature to query database from shell

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)

with app.app_context():
    db.create_all()
