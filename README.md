# Learning Log

A simple web application to track your learning progress. Users can create topics, add entries to those topics, and review their learning history.

## Features
- User authentication (registration, login, logout).
- Add, view, and edit learning topics.
- Add and edit entries for each topic.

## Installation

### Requirements
- Python 3.x
- Django 4.x or later

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/saitsabuncu/learning_log.git
   cd learning_log
   ```

2. **Create and activate a virtual environment:**
   - **For Windows:**
     ```bash
     python -m venv ll_env
     ll_env\Scripts\activate
     ```
   - **For macOS/Linux:**
     ```bash
     python3 -m venv ll_env
     source ll_env/bin/activate
     ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser (optional):**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver
   ```

7. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:8000/`.

## Deployment to Heroku

1. **Install Heroku CLI:**
   Follow the instructions on the [Heroku Dev Center](https://devcenter.heroku.com/articles/heroku-cli) to install the Heroku CLI for your operating system.

2. **Login to Heroku:**
   ```bash
   heroku login
   ```

3. **Create a new Heroku application:**
   ```bash
   heroku create your-app-name
   ```

4. **Add PostgreSQL addon:**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

5. **Set environment variables:**
   ```bash
   heroku config:set SECRET_KEY='your-secret-key'
   heroku config:set DEBUG=False
   ```

6. **Push code to Heroku:**
   ```bash
   git push heroku main
   ```

7. **Apply migrations on Heroku:**
   ```bash
   heroku run python manage.py migrate
   ```

8. **Create a superuser on Heroku (optional):**
   ```bash
   heroku run python manage.py createsuperuser
   ```

9. **Open the application:**
   ```bash
   heroku open
   ```

## Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License.
