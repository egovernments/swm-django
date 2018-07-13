# swm-django

1. Go to the link https://developers.google.com/calendar/quickstart/python and click on enable google calendar api button.
2. Select + Create a new project.
3. Enter the name "Google Calendar API Quickstart".
4. Download the configuration file.
5. Move the downloaded file to your working directory and rename it client_secret.json.

then install the requirements present in requirements.txt by adding pip install infront of all the dependencies

then run the below commands

1. python3 manage.py makemigrations
2. python3 manage.py migrate
3. python3 manage.py loaddata data.json
4. python3 manage.py runserver
