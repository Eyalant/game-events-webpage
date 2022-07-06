from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from os import environ
from dotenv import load_dotenv

app = Flask(__name__)
if not environ.get("is_prod"):
    load_dotenv()

app.config["SQLALCHEMY_DATABASE_URI"] = environ.get("DB_URI")
db = SQLAlchemy(app)

@app.route("/")
def splash_page():
    from events_io import db_init, read_events_from_file, get_all_events
<<<<<<< HEAD
    db_init(read_events_from_file(path_to_file="")) # can run just once for the most part
=======
    # db_init(read_events_from_file(path_to_file=""))
>>>>>>> 7454dc1 (replaced app.py)
    return render_template("bootstrap/album-rtl/index.html", events=get_all_events())
