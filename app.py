import os
from pprint import pprint
from datetime import datetime

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

    return render_template("workout.html", workout_list=workout_list)


@app.route("/workout/create", methods=["GET", "POST"])
def create_workout():
    """
    Create new workout, receive form data and create new DB record
    :return: [status]
    """
    exercise_list = list(mongo.db.exercises.find())

    if request.method == "POST":
        if request.method == "POST":

            submit = {
                "workout_name": request.form.get("workout_name"),
                "workout_sets": request.form.get("workout_sets"),
                "workout_reps": request.form.get("workout_reps"),
                "exercise_choices": request.form.getlist("exercise_choices"),
                "weight": request.form.get("weight"),
                "created_date": datetime.now().strftime("%d/%m/%Y"),
                "modified_date": datetime.now().strftime("%d/%m/%Y"),
                'completed': False,
                'saved': False,
                "created_by": "admin"  # session["user"]
            }

            # print("submit", submit)
            mongo.db.routines.insert_one(submit)
            flash("Workout Successfully Created")
            print("Workout Successfully Created")
            return redirect(url_for("get_workout"))
    return render_template("create_workout.html",  exercise_list=exercise_list)


@app.route("/workout/edit/<workout_id>", methods=["GET", "POST"])
def edit_workout(workout_id):
    """
    Edit existing workout. Takes arguments: [workout_id], query DB, update DB with new data,
    :return: [status]
    """
    if request.method == "POST":
        is_completed = True if request.form.get("is_completed") else False
        is_saved = True if request.form.get("is_saved") else False
        submit = {
            "workout_name": request.form.get("workout_name"),
            "workout_sets": request.form.get("workout_sets"),
            "workout_reps": request.form.get("workout_reps"),
            "exercise_choices": request.form.getlist("exercise_choices"),
            "modified_date": datetime.now().strftime("%d/%m/%Y"),
            "weight": request.form.get("weight"),
            'completed': is_completed,
            'saved': is_saved,
            "created_by": "admin" #session["user"]
        }

        mongo.db.routines.update({"_id": ObjectId(workout_id)}, submit)
        flash("Workout Successfully Updated")
        print("Workout Successfully Updated")

    # print(request.form)
    single_workout = mongo.db.routines.find_one({"_id": ObjectId(workout_id)})
    exercise_list = list(mongo.db.exercises.find())
    return render_template("edit_workout.html", workout_list=single_workout, exercise_list=exercise_list)


@app.route("/workout/<workout_id>", methods=["GET", "POST"])
def delete_workout():
    pass


@app.route("/exercise")
def get_exercise_list():
    """
        Display list of exercises
    """
    exercise_list = list(mongo.db.exercises.find().sort("exercise_name", 1))
    return render_template("exercise_all.html", exercise_list=exercise_list)


@app.route("/exercise/<exercise_id>")
def get_exercise(exercise_id):
    """
        Display individual exercise
    """
    single_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    return render_template("exercise_single.html", exercise=single_exercise)


@app.route("/exercise/edit/<exercise_id>", methods=["GET", "POST"])
def edit_exercise(exercise_id):
    pass



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
