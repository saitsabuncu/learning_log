Learning Log Project

Overview

The Learning Log project is a web application built using Django, designed to help users track their learning progress. Users can create topics, add entries under each topic, and edit these entries as needed. The project is well-suited for personal use or as a learning exercise for those diving into Django and web application development.

Features

User Authentication (Registration, Login, Logout)

Topic Management

Create, View, and Manage topics

Entry Management

Add, Edit, and View entries under specific topics

User-friendly Interface styled with Bootstrap (via CDN)

Deployment-ready for platforms like Heroku

Technologies Used

Backend Framework: Django (Python)

Frontend Framework: Bootstrap 5 (via CDN)

Database: SQLite (default Django database; configurable for PostgreSQL or others)

Deployment: Compatible with Heroku (Heroku CLI and configurations included)

Requirements

Before running this project, ensure the following dependencies are installed:

Local Environment

Python 3.10+

pip (Python package manager)

Django 4.2+

Virtualenv (optional but recommended)

Heroku Deployment

Heroku CLI

Gunicorn (for production WSGI server)

PostgreSQL (via Heroku addon)

Setup and Installation

1. Clone the Repository

$ git clone https://github.com/saitsabuncu/learning_log.git
$ cd learning_log

2. Create a Virtual Environment

$ python -m venv ll_env
$ source ll_env/bin/activate   # On Windows: ll_env\Scripts\activate

3. Install Dependencies

$ pip install -r requirements.txt

4. Run Database Migrations

$ python manage.py makemigrations
$ python manage.py migrate

5. Create a Superuser (Optional for Admin Access)

$ python manage.py createsuperuser

6. Start the Development Server

$ python manage.py runserver

Access the app at http://127.0.0.1:8000/.

Deployment to Heroku

1. Install Heroku CLI

Follow the instructions on Heroku's official documentation.

2. Login to Heroku

$ heroku login

3. Create a New Heroku App

$ heroku create

4. Add PostgreSQL Addon

$ heroku addons:create heroku-postgresql:hobby-dev

5. Push to Heroku

$ git push heroku main

6. Run Migrations on Heroku

$ heroku run python manage.py migrate

Project Structure

learning_log/
├── learning_logs/         # Main app for topic and entry management
├── users/                 # App for user authentication
├── templates/             # HTML templates
├── static/                # Static files (CSS, JavaScript)
├── db.sqlite3             # Default SQLite database
├── requirements.txt       # Python dependencies
├── Procfile               # Heroku process file
├── runtime.txt            # Specifies Python version for Heroku
└── manage.py              # Django project manager

Known Issues and Improvements

Known Issues

Some pages may lack detailed error handling.

Static files are not optimized for production.

Suggested Improvements

Add detailed validation for form inputs.

Optimize the deployment setup for production (e.g., use WhiteNoise for static files).

Implement testing using Django's unittest framework.

Expand user roles and permissions.

Enhance the UI for better user experience.

Contributing

Feel free to fork the repository and make your improvements. Pull requests are welcome!

License

This project is licensed under the MIT License - see the LICENSE file for details.

Contact

For any inquiries, please contact Mustafa Sait.
