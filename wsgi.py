from rosebit_api.api import create_app
from rosebit_api.extensions import db
from rosebit_api.models.model import Users

app = create_app("development")


with app.app_context():
    db.create_all()


#   configure shell feature to query database from shell

@app.shell_context_processor
def make_shell_context():
    return dict(db=db, Users=Users)
