# Fitness Master

![GitHub contributors](https://img.shields.io/github/contributors/alexandergrib/fitness_master)
![GitHub last commit](https://img.shields.io/github/last-commit/alexandergrib/fitness_master)
![GitHub language count](https://img.shields.io/github/languages/count/alexandergrib/fitness_master)
![GitHub top language](https://img.shields.io/github/languages/top/alexandergrib/fitness_master)
![Font Awesome version](https://img.shields.io/badge/Font%20Awesome-v5.15.1-blue)
![Total lines](https://img.shields.io/tokei/lines/github/alexandergrib/fitness_master)

# Fitness Master

Fitness master is the website that have a target auditory who love going to the gym and like to keep tracking of their activity by storing their exercise data.
Where they can explore different exercises or be able to create their own .




## Contents
<p align="center">
  <img width="40%" src= "static/images/headerImg.PNG">
</p>
 
<p align="center"><a href= 'http://fitness-master.herokuapp.com/' target = "_blank">
Fitness Master</a></p>
 
## Table of Contents
 
- [About](#About)
- [User Experience (UX)](#User-Experience-(ux))
  - [User Stories](#User-Stories)
  - [UI](#ui)
  - [Design](#Design)
  - [Database Schema](#database-schema)
  - [Database Model](#database-model)
  - [Wireframes](#Wireframes)
- [Features](#Features)
    - [Future features](#Future-updates)
- [Technologies used](#Technologies-used)
- [Testing](#Testing)
    - [Manual testing](#Testing)
    - [Errors](#Errors)
- [Code Notes](#Code-Notes)
- [Deployment](#Deployment)
- [Credits](#Deployment)
    - [Code](#Code)
     - [Images](#Images)
- [Acknowledgements](#Acknowledgements)

---
## About
The purpose of this project was to build an app where users can tailor their exercise routines to suit their need and keep record of their achievements.


## User Experience (UX)

---

### User Stories

  * Create personalized workout routines
  * Have selection exercises to choose from
  * Be able to read about each individual exercise in details, how to do it, and which area of the body it targets
  * Be able to add my own exercises or modify existing ones to suit my needs
  * Be able to track my workout by monitoring amounts of reps, sets and weight
  * Be able to save my progress 
  * Be able to review my progress
  * Be able to see my workout history(Names) in my profile
  * Be able to see my workout history in details (Expandable details)
  * Be able to see graphs of progress on weight on each exercise

    

### UI

  * A responsive and top attached Navbar.
  * Form to add individual exercise.
  * Form to add individual workout.
  * A search function for users to find exercise based on search criteria.
  * Form to modify a exercise.
  * Form to modify workout.
  * Graphs to display user progress.
  * A registration/login form.
  * A loading page was implemented to stop poor impressions from data loading slowly.
  * A footer to provide some information and social links.

### Design

  * The design of the website  is minimalistic but eye catching using sport themed background.
  * Main page has a nice image background as well as displaying an example of the fitness activity snapshot from user profile to catch attention of the new visitors.
  * At the bottom of the page Register button displayed for the new users or Profile button for the logged-in users.
  * Links and buttons have a hover effect.
  * Exercise/workout containers have a background shadow to stand out from the page.


### Wireframes
Wireframes are my initial design, so you may notice that final website design does not contain everything that was planned at the start of the project.
Some missing features are possible future improvements for the project. They may be implemented at the later stage.
<link to wireframes screenshots>

### Database Schema

I started planning database after I have done my wireframes to justify which fields I would require and what collections I would have to use.
After initial discussion with my mentor I have settled with current database schema.
 * link to pdf file where each collection described in details

### Database Model

 * link to pdf file with db model screenshot


#### CRUD

HTTP Verb | URL PATH | PURPOSE
| --- | --- | --- |
GET | /workout | List All workouts
POST | /workout/create | Create workout
POST | /workout/edit/<:id> | Update workout
DELETE | /workout/delete/<:id> | Delete workout
GET | /workout/start/<:id> | Start Workout
POST | /workout/start/update/:data | Update exercise data inside workout 
GET | /exercise | List All exercises
POST | /exercise/create | Create exercise
GET | /exercise/<:id> | Show individual exercise
POST | /exercise/edit/<:id> | Update exercise
DELETE | /exercise/delete/<:id> | Delete exercise
POST | /register | Register new user
GET | /login | Login user
GET |  /profile/ | User profile
GET | /logout | Logout user





---

## Features

* Ability to Signup/login.
* Ability to Add an exercise.
* Ability to Edit exercise.
* Ability to delete exercise.
* Ability to show/hide system exercises
* When modifying system exercise, that exercise gets cloned and derived from original.
* User unable to delete system exercises
* Ability to Add a workout.
* Ability to Edit workout.
* Ability to delete workout.
* A loading page.
* Ability to save current workout session statistics for individual exercise whiting that workout.
* Ability to view statistics for the last 5 sessions for each exercise whiting workout.
* A fully functioning search for exercises based on either exercise name or description text(word/phrase).
* Ability to view historical weight progress for each exercise.
* The project contains a few security features, such as:
  * validating login.
  * hashing passwords.
  * environment variables are hidden.
  * debug is turned off in the production version.


###  Future updates

1. a
2. b
3. c

---
 
## Technologies used

Below I have listed the programming languages, technologies, frameworks and resources used for this project.
 
* **HTML5**
* **CSS3**
* **Vanilla JS**
* **J Query**
* **Markdown**
* **Git** for version control.
* **Github** to hold my project.
* **Heroku** to deploy my project to the web.
* **Flask**
* **MongoDB**
* **Google Chrome/FireFox/Edge/Safari** 
* **Developer tools for chrome/FireFox/Edge**
* **[Amiresponsive](http://ami.responsivedesign.is/)**
* **[Balsamiq](https://balsamiq.com/)** to create wireframes.
* **[W3Schools](https://www.w3schools.com/)** for help with some issues I ran into
* **[StackOverFlow](https://stackoverflow.com/)** for help with some issues I ran into
* **Mentor** my code institute mentor for advice
* **[Slack](https://slack.com/)** specifically the code institute room in slack.
* **[Grammarly](https://www.grammarly.com/)** to correct grammar and spelling mistakes.
* **[Charts CSS](https://chartscss.org/)** to display charts for each workout completed
* **[Stackoverflow](https://stackoverflow.com)** to help me solve unsolvable

---

## Testing

* [HTML validator](https://validator.w3.org/#validate_by_input)
* [CSS validator](https://jigsaw.w3.org/css-validator/#validate_by_input)
* [JsHint](https://jshint.com)
* Testing [checklist](https://geteasyqa.com/qa/test-website/)
* [pep8](http://pep8online.com/)
 
I personally tested the website on some of my own personal systems of which include:
1.
2.


### Manual testing  (need rework)
<details>
<summary>
Testing conducted
</summary>

N | Section | Test | Result
|:---:|---|---|:---:|
1 | User account | Create an account, works as it should, passwords are hashed for security. |  &#9745;
2 | User account | Logging in to the created account. | &#9745;
3 | User account | Logout functionality. | &#9745;
4 | Exercises | Adding new exercise, works as it should. Adding new exercise possible to only logged-in user  |  &#9745;
5 | Exercises | * System and user exercises are displayed.<br> * Turning off "Show system exercises" hides all non user records. <br>    *  State of the switch preserved if the page get reloaded  |  &#9745;
6 | Exercises |  Search for full exercise name or a full word whiting the description working as it should. <br>   *(Partial text is not functioning at the moment example: full word "food", searching for "foo" would not show any result) |  &#9745;
7 | Exercises | Clicking on exercise card will take to exercise detailed info |  &#9745;
8 | Exercises/edit |  Clicking "EDIT" link whiting detailed exercise info page will take user to the form page where user can update any field |  &#9745;
9 | Exercises/edit | Update any fields whiting EDIT exercise page press "UPDATE EXERCISE" button: <br> - results gets updated <br> - Flash message displayed  |  &#9745;
10 | Workouts | Create new workout functionality |  &#9745;
11 | Workouts/create | Pick exercises are displaying user and system exercises |  &#9745;
12 | Workouts | Click on newly created workout card, takes you to "Start workout" page  |  &#9745;
13 | Workouts/start | All selected workouts are displayed |  &#9745;
14 | Workouts/start |  On any exercise card dial "reps" and "weight" then press to "add to session" button <br> 1. "current session" will display newly added line <br> 2. Repeat previous step to add few more <br> 3. Press "complete exercise" to save progress <br> 4. Newly saved progress would be displayed on the "Last 5 set" section |  &#9745;
15 | Workouts/profile | Displaying username  |  &#9745;
16 | Workouts/profile | Displaying latest workout weights progress  |  &#9745;

 
No automated testing was conducted.
</details>

### Errors
<details>
<summary>
Current errors:
</summary>

1. ***FIXED***  ~~issue with static directory, images have to be in static/css~~ -- fixed, file structure error.
2. When deleting exercise, its name still shown in the workout card, until this card get modified by user and new exercises are reselected.
    * Left as it is at the moment.
    * Possible fix, query db when deleting exercises, and remove record from workout list containing that exercise.
    * Better solution to use relational DB in the future.
4. fixed
5. fixed
6. fixed
</details>

---
## Code Notes

---

## Deployment

<details>
<summary>
Deployment
</summary>

To deploy this project I used [Heroku](https://dashboard.heroku.com/)

**The final version of the application was deployed using Heroku:**   
**[here](https://fitness-master.herokuapp.com/)**

The deployed version is the same version as in the repository.

The following steps were used for deployment on Heroku:

1. In Gitpod CLI, in the root directory of the project, run 

   `pip3 freeze --local > requirements txt`

   to create a `requirements.txt` file containing project dependencies.

2. In the Gitpod project workspace root directory, create a new file called Procfile, with capital 'P'.  
   Open the Procfile. Inside the file, enter:  

   `web: python3 app.py`

    Save the file.

3. **Make sure you do a Git commit after creating the requirements.txt and the Procfile.**

4. On [Heroku](https://www.heroku.com/), sign in using your username and password.

5. On Heroku Dashboard, press the "New" button, then select "Create new app".

6. Enter the name of your app and select your region.   
   Press "Create app".

7. On Heroku App Dashboard, select the Settings tab.

    Under "App information", copy the Heroku git URL.

8. In Gitpod workspace CLI, in the project's root directory, enter  

    `heroku login`   

    Follow the instructions to login.

    Enter 

    `git remote add heroku <Heroku Git URL>`

    where `<Heroku Git URL>` is the Heroku git URL copied from the Heroku App Dashboard in Settings (step 7 above).

    Finally, enter

    `git push heroku master`

    to push the contents of your local Git repository to the newly created Heroku remote repository.

9. Still in the Gitpod workspace CLI, enter 

     `heroku ps:scale web=1`
        
     to start the Heroku web process.

10. Log into your [MongoDB Atlas](https://account.mongodb.com/account/login) account.   

    In the dashboard, select your database Cluster, then click the Connect button.

    In the pop-up, select the option "Connect your application". 

    Under the tab "Connection string only", copy the connection string.

11. Login into [Cloudinary](https://cloudinary.com/) account.
    
    In the dashboard copy your cloud name, API key and API Secret

12. On Heroku App Dashboard, in the Settings tab, click the button "Reveal Config vars".

    Using the Add button, add the following keys and their corresponding values:

    key: `IP`  
    value: `0.0.0.0`

    key: `PORT`   
    value: `5000`   
    
    key: `MONGO_URI`   
    value:   
    - paste the string copied from MongoDB,
    - inside the pasted string, replace `<password>` with your database access password (**NOT** your MongoDB login password),
      ensure you remove the `<>`.
    - replace `test` with the name (case-sensitive!) of the database used for your project.

    key: `SECRET_KEY`   
    value: value of SECRET_KEY as entered in the project's env.py file, **without quotes** . 

13. Whilst in the "Config vars" section add the rest of the required [Cloudinary](https://cloudinary.com/) requirements.
    
    key:cloud_name
    value: <your cloud name>

    key: api_key
    value:  "<api value>"

    key: api_secret
    value:  "<secret value>"

14. In the top right corner of the Heroku App Dashboard, click on the More button.

    From the dropdown menu, select "Restart all dynos". Confirm Restart when prompted. 

15. Click on Open app. The App is now deployed.
</details>

### Local Deployment
<details>
<summary>
If you want to run this project locally, you will need to follow these steps.
</summary>

1. Clone or download this repository.

2. Upload the repository into your IDE of choice.  

I used Gitpod for development, so the following steps will be specific to Gitpod. You will need to adjust them depending on your IDE.

3. In your workspace CLI, run

   `pip3 install -r requirements.txt`

   to install the project-required dependencies.

4. In the root directory of your project, create an env.py file. 

   Don't forget to add the env.py file to your .gitignore file.

5. In MongoDB Atlas, create a new database for the project.

    The database needs to have the following attributes:

    - collection "categories"
    - collection "exercises"
    - collection "routines"
    - collection "user_profile"
    - collection "users"
   
    In collection "categories":
    - document property: "category_name" -> String
    - document property: "img" -> String

    In collection "exercises":
    - document property: "about" -> String
    - document property: "created_by" -> String
    - document property: "exercise_comments" -> String
    - document property: "exercise_name" -> String
    - document property: "exercise_reps" -> String
    - document property: "img_url" -> String
    - document property: "is_system" -> Boolean
    - document property: "modified_date" -> String
    - document property: "steps" -> Array
    - document property: "weight" -> String
    - document property: "yt_url" -> String
    - document property: "exercise_sets" -> String
    - document property: "exercise_category" -> List
    - document property: "origin" -> String
    - document property: "exercise_history" -> List

    In collection "routines":
    - document property: "completed" -> Boolean
    - document property: "created_date" -> String
    - document property: "exercise_choices" -> Array 
    - document property: "modified_date" -> String
    - document property: "saved" -> Boolean
    - document property: "weight" -> String
    - document property: "workout_name" -> String
    - document property: "workout_reps" -> String
    - document property: "created_by" -> String
    - document property: "workout_sets" -> String

    In collection "user_profile":
    - document property: "comment" -> String
    - document property: "date" -> String
    - document property: "exercise_id" -> String
    - document property: "exercise_name" -> String
    - document property: "reps" -> String
    - document property: "username" -> String
    - document property: "weight" -> String
    - document property: "workout_name" -> String
    - document property: "workout_id" -> String

6. Once you have created the database, go back to the Cluster View and click "Connect".
    In the resulting pop-up, click on "Connect your application".
    Under the tab "Connection String Only", copy the connection string.

7. Back in your IDE, open the env.py file.

   At the top of the file, add 

   `import os`

   Then, add 

   `os.environ["MONGO_URI"] = "<mongo_uri>"`
    
    where `<mongo_uri>` is the pasted MongoDB connection string copied in step 6 above.

   In the pasted `<mongo_uri>` string:
   - replace < password > with your database access password (**NOT** your MongoDB login password), and
   - replace "test" with the name (case-sensitive!) of your project database. 

   Finally, add

   `os.environ["SECRET_KEY"] = "<your_secret_key>"`

    where `<your_secret_key>` is a combination of letters, numbers and characters of your choice. This is used to enable the Flask flash messaging feature.

    

8. Login into [Cloudinary](https://cloudinary.com/) account.
    
    In the dashboard copy your cloud name, API key and API Secret
    
    Add them to your env.py
   1. `os.environ["cloud_name"] = "<your_cloud_name>"`
   2. `os.environ["api_key"] = "<your_api_key>"`
   3. `os.environ["api_secret"] = "<your_api_secret>"`
   
    Save the file.

9. Run the app.py file and open it in your browser.   
    The application is now running locally.
</details>

---
## Credits
### Code


### Images

* All background images came from [Google-Images](https://www.google.com/imghp?hl=en)


---


## Acknowledgements
 
A thank you to my friends and family for testing the website for me.
Also a thank you to my mentor for the help and support.
[Aidan](https://github.com/aidant842/MilestoneProject3) for his README template
[Back to top ↑](#fitness-master)





















Sources credits

image placeholders https://placehold.it/250x500

https://images.unsplash.com/photo-1623200216581-969d9479cf7d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjl8fHN0cmV0Y2h8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60
Photo by <a href="https://unsplash.com/@helloatma?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Anastasia Hisel</a> on <a href="https://unsplash.com/s/photos/stretch?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
Photo by <a href="https://unsplash.com/@victorfreitas?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Victor Freitas</a> on <a href="https://unsplash.com/s/photos/old-empty-gym?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

problems encountered:

- Was trying to create mongoDB query filter where i have system created exercises and user able to modify system exercise by cloning it. As a result i have system and user modified with the similar/same name, and both are displayed to user. I was unable to create filter which will hide system exercises once they are cloned by user. After spending hours in search for solution i decided to go in different aproach.
Now user still able to clone system exercises and they are both displyaed to user, but i gave user an option to hide all system exercises on the thml page.