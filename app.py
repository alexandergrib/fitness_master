import os
import re
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


from helpers import upload_image

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
            "created_by": "admin"  # session["user"]
        }

        mongo.db.routines.update({"_id": ObjectId(workout_id)}, submit)
        flash("Workout Successfully Updated")
        print("Workout Successfully Updated")
        return redirect(url_for("get_workout"))

    # print(request.form)
    single_workout = mongo.db.routines.find_one({"_id": ObjectId(workout_id)})
    exercise_list = list(mongo.db.exercises.find())
    return render_template("edit_workout.html", workout_list=single_workout, exercise_list=exercise_list)


@app.route("/workout/delete/<workout_id>", methods=["GET", "POST"])
def delete_workout(workout_id):
    mongo.db.routines.remove({"_id": ObjectId(workout_id)})
    flash("Workout Successfully Deleted")
    return redirect(url_for("get_workout"))


@app.route("/workout/start/<workout_id>", methods=["GET", "POST"])
def start_workout(workout_id):
    """
    Start existing workout. Takes arguments: [workout_id], query DB,
        :return data
    """
    
    single_workout = mongo.db.routines.find_one({"_id": ObjectId(workout_id)})
    exercise_list = list(mongo.db.exercises.find())
    return render_template("start_workout.html",
                           workout_list=single_workout,
                           exercise_list=exercise_list)




@app.route("/workout/start/update/<query>", methods=["POST", ])
def update_workout_data(query):
    if request.method == "POST":
        exercise_data = mongo.db.exercises.find_one({"_id": ObjectId(query)})
        exercise_history = (exercise_data["exercise_history"] +
                            request.form.getlist("info_"+query+"[]"))

        print(exercise_history)
        submit = {
            "exercise_name": exercise_data["exercise_name"],
            "description": exercise_data["description"],
            "about": exercise_data["about"],
            "img_url": exercise_data["img_url"],
            "exercise_sets": exercise_data["exercise_sets"],
            "exercise_reps": request.form.get("reps_"+query),
            "exercise_category": exercise_data["exercise_category"],
            "modified_date": datetime.now().strftime("%d/%m/%Y"),
            "weight": request.form.get("weight_"+query),
            'exercise_comments': exercise_data["exercise_comments"],
            'yt_url': exercise_data["yt_url"],
            'steps': exercise_data["steps"],
            "created_by": exercise_data["created_by"],
            "exercise_history": exercise_history  # request.form.getlist("info_"+query+"[]")
        }
        id = request.form.get("id_"+query)
        # print(submit['exercise_history'])

        mongo.db.exercises.update({"_id": ObjectId(query)}, submit)

        return redirect(url_for("start_workout", workout_id=id))


#---------------------------------exercise section


@app.route("/exercise")
def get_exercise_list():
    """
        Display list of all exercises
    """
    exercise_list = list(mongo.db.exercises.find().sort("exercise_name", 1))
    return render_template("exercise_all.html", exercise_list=exercise_list)




@app.route("/exercise/create", methods=["GET", "POST"])
def create_exercise():
    """
    Create new exercise

    exercise_name,
    category,
    description,
    img_url,
    exercise_sets,
    exercise_reps,
    weigth,
    exercise_comments,
    yt_url,
    steps{array}
    about

    """
    if session["user"]:
        username = session["user"]
    else:
        username = "admin"

    exercise_category_list = list(
        mongo.db.categories.find().sort("category_name", 1))
    if request.method == "POST":
        yt = request.form.get("yt_url")
        replace_url = re.sub(r'^[a-zA-Z]+\W+\w+.\w+\/', 'https://youtube.com/embed/', yt)
        img_url = request.form.get("img_url")
        
        try:
            img_cdn = upload_image(img_url)
        except KeyError:
            img_cdn = "https://via.placeholder.com/250"
        
        print(img_cdn)
        submit = {
            "exercise_name": request.form.get("exercise_name"),
            "description": request.form.get("description"),
            "about": request.form.get("about"),
            "img_url": img_cdn,  # request.form.get("img_url"),
            "exercise_sets": request.form.get("exercise_sets"),
            "exercise_reps": request.form.get("exercise_reps"),
            "exercise_category": request.form.getlist("exercise_category"),
            "modified_date": datetime.now().strftime("%d/%m/%Y"),
            "weight": request.form.get("weight"),
            'exercise_comments': request.form.get("exercise_comments"),
            'yt_url': replace_url,   
            'steps': request.form.getlist("steps"),
            "created_by": username
        }

        mongo.db.exercises.insert_one(submit)
        print(submit)
        flash("Exercise Successfully Created")
        print("Exercise Successfully Created")
        return redirect(url_for("get_exercise_list"))

    return render_template("create_exercise.html",
                           exercise_category_list=exercise_category_list)


@app.route("/exercise/<exercise_id>")
def get_exercise(exercise_id):
    """
        Display individual exercise
    """
    single_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    return render_template("exercise_single.html", exercise=single_exercise)


@app.route("/exercise/edit/<exercise_id>", methods=["GET", "POST"])
def edit_exercise(exercise_id):
    """
        Modify individual exercise
    """
    if session["user"]:
        username = session["user"]
    else:
        username = "admin"
    exercise_category_list = list(
        mongo.db.categories.find().sort("category_name", 1))
    single_exercise = mongo.db.exercises.find_one({"_id": ObjectId(exercise_id)})
    if request.method == "POST":
        yt = request.form.get("yt_url")
        replace_url = re.sub(r'^[a-zA-Z]+\W+\w+.\w+\/', 'https://youtube.com/embed/', yt)
        img_url = request.form.get("img_url")
        
        try:
            img_cdn = upload_image(img_url)
        except KeyError:
            img_cdn = "https://via.placeholder.com/250"
        submit = {
            "exercise_name": request.form.get("exercise_name"),
            "description": request.form.get("description"),
            "about": request.form.get("about"),
            "img_url": img_cdn,  #  request.form.get("img_url"),
            "exercise_sets": request.form.get("exercise_sets"),
            "exercise_reps": request.form.get("exercise_reps"),
            "exercise_category": request.form.getlist("exercise_category"),
            "modified_date": datetime.now().strftime("%d/%m/%Y"),
            "weight": request.form.get("weight"),
            'exercise_comments': request.form.get("exercise_comments"),
            'yt_url': replace_url,  # create validator for url
            'steps': request.form.getlist("steps"),
            "created_by": username
        }

        mongo.db.exercises.update({"_id": ObjectId(exercise_id)}, submit)
        pprint(submit)
        flash("Exercise Successfully Updated")
        print("Exercise Successfully Updated")
        return redirect(url_for("get_exercise", exercise_id=exercise_id))
    return render_template("exercise_edit_single.html", exercise=single_exercise,
                           exercise_category_list=exercise_category_list)

@app.route("/exercise/delete/<exercise_id>", methods=["GET", "POST"])
def delete_exercise(exercise_id):
    mongo.db.exercises.remove({"_id": ObjectId(exercise_id)})
    flash("Exercise Successfully Deleted")
    return redirect(url_for("get_exercise_list"))





# -----------------handle login logout register


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists in db
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches user input
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                        session["user"] = request.form.get("username").lower()
                        flash("Welcome, {}".format(
                            request.form.get("username")))
                        return redirect(url_for(
                            "profile", username=session["user"]))
            else:
                # invalid password match
                flash("Incorrect Username and/or Password")
                return redirect(url_for("login"))

        else:
            # username doesn't exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")

@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("profile.html", username=username)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # remove user from session cookie
    flash("You have been logged out")
    session.pop("user")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
