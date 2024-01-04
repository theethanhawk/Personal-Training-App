Personal Training App Description
This app serves as a comprehensive hub for personal training management, addressing the challenge of organizing the extensive information involved in personal training. Traditionally reliant on notebooks, whiteboards, and memory, users can now streamline their fitness journey through our digital solution.

Key features include:

Health Metrics Tracking: Monitor vital health statistics to understand your physical condition better.
Workout Logs: Record and review past workout details, offering a clear view of your exercise routine.
Program Creation: Design personalized training programs tailored to your fitness goals.
Progress Insights: Gain valuable insights into your training effectiveness. The app analyzes data across various activities, helping you track progress and fine-tune your training approach.
Setup and Installation
Requirements
Python (built with Python 3.11.1)
Django (built with Django 5.0)
Installation Steps
Create a Project Folder:
Go to the folder in your command terminal where you would like to store this project and create a folder. Example: mkdir pt_program.

Virtual Environment Setup:
Set up a virtual environment for Python. This is crucial for maintaining project dependencies separately. Follow the steps in this YouTube video for guidance. Note: Virtual environment files are included in the .gitignore and won't be visible in this repository.

Install Django:
Within your virtual environment, install Django using the command: pip install django.

Start the Django Server:
Run python manage.py runserver. Visit the HTTP link shown in the command terminal. You should see a Django success page with links to documentation and community resources.

Building the App
Activate Virtual Environment:
Ensure your virtual environment is active. Reference the YouTube video linked above for assistance.

Start Django Project:
Use the command django-admin startproject [project name] . (The period at the end is crucial for configuration).

Database Migration:
Run python manage.py migrate. This creates a db.sqlite3 file in your project root directory.

Starting the Apps
App Creation:
With the virtual environment active, run python manage.py startapp [app name]. Example: python manage.py startapp dashboard_app.

Register Apps in Settings:
In your IDE, open settings.py in your project folder. Under INSTALLED_APPS, add your created apps like so:

python
Copy code
INSTALLED_APPS = [
    # My apps
    'dashboard_app',
    'goals_app',
    'health_metrics_app',
    'pt_data_app',
    'pt_programs_app',
    'workout_hub_app',

    # Default Django apps
    <-default apps here->
]
After following these steps, your project directory should include the following items:

dashboard_app
db.sqlite3
goals_app
health_metrics_app
manage.py
personal_trainer
pt_data_app
pt_env
pt_programs_app
workout_hub_app
You can now proceed to build the project using the files in this repository.

Commit history:
first commit - included the basic layout of the homepage with links to the different components of the app. Functionality of adding metric data and viewing metric data have been added.
second commit - includes models, forms, and views for goals as well as html for adding and viewing goals.
