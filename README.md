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

### User Stories

    * Create personalized workout routines
    * Have selection exercises to choose from
    * Be able to read about each individual exercise in details, how to do it, and which area of the body it targets
    * Be able to add my own exercises or modify existing ones to suit my needs
    * Be able to track my workout by monitoring amounts of reps, sets and weight

    

### UI
### Design

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


### Database Schema

### Database Model

### Wireframes

---

## Features

###  Future updates

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


### Manual testing
<details>
<summary>
Testing conducted
</summary>

* Create an account, works as it should, passwords are hashed for security. &#9745;
* Logging in to the created account, works as it should. &#9745;
* Adding a game using form, works as it should. Adding a game is only possible when logged in. &#9745;
* Game is displayed on the games page, works well. &#9745;
* Game info is displayed on a separate page when clicked into. Works as it should. &#9745;
* Edit game, works as it should, only editable by the user that submitted it. &#9745;
* Delete game works as it should, only able to delete if you submitted the review. &#9745;
* Add a game button visible in nav if the user is logged in. &#9745;
* Edit/Delete game buttons visible if you are the user who entered the review. &#9745;
* Login and Singup buttons are only visible if you are not signed in. &#9745;
* If the username already exists in the database, prompts the user that it already exists. &#9745;
* If a user enters a login url when already logged in it will redirect to home with a flash message. &#9745;
* Search function, not 100%, returns 505 if no criteria specified(caught with custom 505). [**NOW CORRECTED**]
* All links work. &#9745;
* Games can only be entered once on the database. (checks title) &#9745;
* Developer being added to a separate collection when the user submits a game review if it doesn't already exist in the database. works &#9745;
* Flash messages appear when appropriate to ensure completed action to the user, or if errors occur. &#9745;
* All fields required when adding/editing games so no fields are empty on the game description page. &#9745;
* Correct data is displayed for each field in edit form. &#9745;
* Automatically converts youtube videos to embed to display video in iframe. &#9745;
* Custom 505 error page. &#9745;
* Delete modal appears when the first delete button clicked, and the game only deleted from the database after the Confirmation delete clicked. &#9745;
* Confirm password on signup page works as expected. &#9745;
* Search function works as expected, empty search returns all entries, each criteria can be searched separately.
  Also saves your search criteria after search is complete. &#9745;
 
No automated testing was conducted.
</details>

### Errors
<details>
<summary>
Current errors:
</summary>

1. ***FIXED***  ~~issue with static directory, images have to be in static/css~~ -- fixed, file structure error.
2. fixe
3. fixed
4. fixed
5. fixed
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
**[here](http://gamersdb.herokuapp.com/home_page)**

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

9.  Still in the Gitpod workspace CLI, enter 

     `heroku ps:scale web=1`
        
     to start the Heroku web process.

10. Log into your [MongoDB Atlas](https://account.mongodb.com/account/login) account.   

    In the dashboard, select your database Cluster, then click the Connect button.

    In the pop-up, select the option "Connect your application". 

    Under the tab "Connection string only", copy the connection string.


11. On Heroku App Dashboard, in the Settings tab, click the button "Reveal Config vars".

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

12. In the top right corner of the Heroku App Dashboard, click on the More button.

    From the dropdown menu, select "Restart all dynos". Confirm Restart when prompted.


13. Click on Open app. The App is now deployed.
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

    - collection "age_rating"
    - collection "developer"
    - collection "games"
    - collection "genre"
    - collection "platform"
    - collection "users"
    - collection "vr_capable"

    In collection "age_rating":
    - document property: "rating" -> String

    In collection "developer":
    - document property: "dev" -> String

    In collection "games":
    - document property: "title" -> String
    - document property: "genre_name" -> String
    - document property: "description" -> String
    - document property: "shop_link" -> String
    - document property: "review" -> String
    - document property: "age_rating" -> String
    - document property: "image" -> String
    - document property: "platform" -> String
    - document property: "release_date" -> String
    - document property: "languages" -> String
    - document property: "developer" -> String
    - document property: "trailer_link" -> String
    - document property: "playthrough_time" -> String
    - document property: "vr_capable" -> String
    - document property: "username" -> String

    In collection "genre":
    - document property: "genre_name" -> String

    In collection "platform":
    - document property: "platform_name" -> String

    In collection "users":
    - document property: "name" -> String
    - document property: "password" -> String

    In collection "vr_capable":
    - document property: "vr" -> Boolean


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

    Save the file.

8. Run the app.py file and open it in your browser.   
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
 
[Back to top ↑](#fitness-master)





















Sources credits

image placeholders https://placehold.it/250x500

https://images.unsplash.com/photo-1623200216581-969d9479cf7d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjl8fHN0cmV0Y2h8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60
Photo by <a href="https://unsplash.com/@helloatma?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Anastasia Hisel</a> on <a href="https://unsplash.com/s/photos/stretch?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
Photo by <a href="https://unsplash.com/@victorfreitas?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Victor Freitas</a> on <a href="https://unsplash.com/s/photos/old-empty-gym?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  

problems encountered:

- Was trying to create mongoDB query filter where i have system created exercises and user able to modify system exercise by cloning it. As a result i have system and user modified with the similar/same name, and both are displayed to user. I was unable to create filter which will hide system exercises once they are cloned by user. After spending hours in search for solution i decided to go in different aproach.
Now user still able to clone system exercises and they are both displyaed to user, but i gave user an option to hide all system exercises on the thml page.