![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
---

### 1.) Install two additional dependencies
In order to use our Google Sheets API, we're going to need to install two additional dependencies into our project.
- The first is called google-auth, which will use our creds.json file
to set up the authentication needed  to access our Google Cloud project.
- The second is gspread, which is a library of code  that we will use to access and update data in our spreadsheet.  

Terminal command 'pip3 install gspread google-auth'

### 2.) Heroku deployment
- Front page -> Create new app
- App name + Europe -> Create app
- Dashboard -> Settings tab
- _Config Vars_ called `PORT`. Set this to `8000`
- Config Vars -> Reveal Config Vars -> CREDS + creds.json code
- Buildpacks -> Add buildpack -> Python + Node.js
- Deploy tab -> Deployment method -> GitHub -> Connect to GitHub -> Authorize Heroku
  -> Popup window -> Sign in to GitHub -> Search for gitHub project
- Manual deploy -> Deploy a GitHub branch -> Deploy Branch button
- Receive code from GitHub -> Build main ...
- Your app was successfully deployed. -> View button
- https://lovesandwichestest-3933ba4021f6.herokuapp.com/