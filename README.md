# Learning Log

A simple web application to track your learning progress. Users can create topics, add entries to those topics, and review their learning history.

## Features
- User authentication (registration, login, logout).
- Add, view, and edit learning topics.
- Add and edit entries for each topic.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/saitsabuncu/learning_log.git
   cd learning_log
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv ll_env
   ll_env\Scripts\activate  # On Windows
   source ll_env/bin/activate  # On macOS/Linux
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply migrations and create the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. Run the server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000/`.

## Deployment
To deploy this application to Heroku:
1. Install Heroku CLI.
2. Login to Heroku:
   ```bash
   heroku login
   ```
3. Create a Heroku app and push the code:
   ```bash
   heroku create
   git push heroku main
   ```
4. Add PostgreSQL database and configure environment variables.

## Requirements
- Python 3.x
- Django 4.x or later
- PostgreSQL (for production)
- Bootstrap (for styling)

## Contributing
Feel free to fork the repository and submit pull requests. Contributions are welcome!

## License
This project is licensed under the MIT License.
```
