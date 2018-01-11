from flask import Flask, render_template, session, request, flash, redirect, url_for
from socket import gethostname
import random

app = Flask(__name__)

app.config.from_object('config')

CSRFProtect(app)

db = SQLAlchemy(app)

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/logos")
def newGame():
	return render_template('logos.html')

@app.errorhandler(404)
def page_not_found(e):
    """Return a custom 404 error."""
    return 'Sorry, nothing at this URL.', 404

if __name__ == "__main__":
	#db.create_all()
	if 'liveconsole' not in gethostname():
		app.run(debug = True)
    #app.run()

