# ezwashing

ezwashing is a simple web application that I created to tell me the status of the washing machines in my apartment building. It  scrapes the status of each machine from the [ezwashing.com](http://ezwashing.com) site but without the annoying requirement to log in every few minutes.

It pulls html down with the requests module, then processes it with Beautiful Soup. Jinja is then used for HTML templating and adds a class to the HTML elements based on the status of each machine. If the machine is available then it will be stationary with a green status button. If it's busy then the status button will be red and a CSS animation is used to shake the machine.

## Developing locally
1. Clone repo
2. python3 -m venv env
3. source env/bin/activate
4. pip3 install -r requirements.txt
5. Edit ezwashing/config.py and add a username and password (you need to create one on ezwashing.com)
6. Edit run.py and change app.run() to app.run(debug=True)

Make sure to undo steps 5 and 6 when pushing code back to github.

## Deploying the app

### Heroku
1. Clone the repo
2. python3 -m venv env
3. source env/bin/activate
4. pip3 install gunicorn
5. pip3 freeze > requirements.txt
6. vi Procfile and add this text:
- web: gunicorn run:app
7. Create a new heroku app on the dashboard
8. Follow the rest of the commands on the heroku dashboard to deploy

## To Do
- create a config route to edit config.py
- create a scheduled task, say every minute to update machine status, rather run those functions on each page reload
- figure out how to scrape the id names from html in a more automated way (right now they are all hardcoded with the washer/dryers in my building)
