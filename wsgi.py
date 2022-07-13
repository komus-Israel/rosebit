from rosebit_api.api import create_app

app = create_app("development")


#   configure shell feature to query database from shell

#@app.shell_context_processor
def make_shell_context():
    return
