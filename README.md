Django Authenticated To-Do Application

A simple, robust, and full-featured To-Do list application built using the Django framework. This project includes user authentication (registration, login, and logout) to ensure that each user's to-do list remains private and secure.

🌟 Features

User Authentication: Secure user registration, login, and logout functionalities managed by Django's built-in authentication system.

Private To-Do Lists: Each user can only view and manage their own tasks.

CRUD Operations:

Create: Easily add new tasks to the list.

Read: View all active and completed tasks.

Update: Edit existing task details.

Delete: Remove tasks permanently.

Task Management: Mark tasks as completed to track progress.

Database Persistence: Tasks and user data are stored securely using Django's ORM and an SQLite (default) or PostgreSQL database.

🚀 Prerequisites

Before you begin, ensure you have the following installed on your system:

Python: Version 3.8 or higher.

pip: Python package installer (usually included with Python).

🛠️ Installation and Setup

Follow these steps to get a local copy up and running:

1. Clone the repository

git clone [https://github.com/Xenawi/django_app.git](https://github.com/Xenawi/django_app.git)
cd django-todo-app


2. Create and activate a virtual environment

It's highly recommended to use a virtual environment to manage dependencies.

On macOS/Linux:

python3 -m venv venv
source venv/bin/activate


On Windows:

python -m venv venv
.\venv\Scripts\activate


3. Install dependencies

Install the necessary Python packages using the provided requirements.txt file (assuming you have one, which is standard for Django projects).

pip install -r requirements.txt


4. Database Setup

Apply the database migrations to set up the necessary tables (including Django's authentication tables and your To-Do models).

python manage.py migrate


5. Create a Superuser (Optional)

You can create an administrative user to access Django's built-in Admin interface:

python manage.py createsuperuser


Follow the prompts to set a username, email, and password.

💻 Usage

1. Start the development server

python manage.py runserver


2. Access the application

Open your web browser and navigate to the following address:

http://127.0.0.1:8000/

3. Register and Log In

Go to /register or click the 'Sign Up' link to create a new user account.

Log in using your new credentials.

Once logged in, you can start managing your private To-Do list!

💡 Technology Stack

Backend:  Django (Python Web Framework)

Database: SQLite (Default for development)

Frontend: HTML5, CSS3, Vanilla JavaScript (or Tailwind CSS/Bootstrap if used)

📄 License

This project is licensed under the MIT License - see the LICENSE.md file for details.
