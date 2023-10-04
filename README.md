# To run locally:
## Create a Python virtual environment:
> python -m venv djangoenv
## Activate virtual environment:
> source djangoenv/Scripts/activate
## Clone repository:
> https://github.com/dcierra/severstal_notes_app.git
## cd to directory:
> cd severstal_notes_app/notes_project
## Install requirements:
> pip install -r requirements.txt
## Copy .env.example to .env:
> cp .env.example .env
## fill .env
## Make migrations:
> python manage.py makemigrations
## Migrate:
> python manage.py migrate
## Create a superuser:
> python manage.py createsuperuser
## Run server:
> python manage.py runserver
