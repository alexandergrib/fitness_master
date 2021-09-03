![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome alexandergrib,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. The last update to this file was: **July 2, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.



**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

---

Happy coding!



Sources credits

image placeholders https://placehold.it/250x500

https://images.unsplash.com/photo-1623200216581-969d9479cf7d?ixid=MnwxMjA3fDB8MHxzZWFyY2h8Mjl8fHN0cmV0Y2h8ZW58MHx8MHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60
Photo by <a href="https://unsplash.com/@helloatma?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Anastasia Hisel</a> on <a href="https://unsplash.com/s/photos/stretch?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>


problems encountered:

- Was trying to create mongoDB query filter where i have system created exercises and user able to modify system exercise by cloning it. As a result i have system and user modified with the similar/same name, and both are displayed to user. I was unable to create filter which will hide system exercises once they are cloned by user. After spending hours in search for solution i decided to go in different aproach.
Now user still able to clone system exercises and they are both displyaed to user, but i gave user an option to hide all system exercises on the thml page.