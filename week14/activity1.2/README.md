# Week 14 – Activity 1.2: Hello Django

A basic Django web application that displays **Hello Django** in a web browser.

## Requirements

- Python 3.13
- Django 6.0.7
- Conda environment: `django-env`

## Setup

Open Anaconda Prompt and run:

```powershell
conda activate django-env
cd C:\Users\User\Documents\GitHub\MSE800\week14\activity1.2
python -m pip install -r requirements.txt
```

Apply the database migrations:

```powershell
python manage.py migrate
```

## Run the application

```powershell
python manage.py runserver
```

Open <http://127.0.0.1:8000/>. The page displays **Hello Django**.

Stop the development server with `Ctrl+C`.

## Test the application

```powershell
python manage.py check
python manage.py test
```

## Project structure

```text
activity1.2/
├── hello/          # Application view, URL configuration, and tests
├── hello_django/   # Django project settings and root URL configuration
├── manage.py       # Django command-line utility
├── requirements.txt
└── README.md
```
