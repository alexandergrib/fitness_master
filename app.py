import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

# conn = mongo.db.exercises
# exercise_coll = conn["fitness_master"]["exercises"]
# routine_coll = conn["fitness_master"]["routines"]
# categories_coll = conn["fitness_master"]["categories"]

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/workout")
def get_workout():
    """Display workout html page. Takes arguments: ,Returns:  """
    workout_list = list(mongo.db.routines.find().sort("routine_name", 1))
    # categories = list(mongo.db.categories.find().sort("category_name", 1))
    # return render_template("categories.html", categories=categories)

    return render_template("workout.html", workout_lsit=workout_list)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
