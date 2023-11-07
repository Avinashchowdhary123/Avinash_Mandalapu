Clone the repository

install dependencies:pip install django

Create django Project with command : django-admin startproject firstname_lastname

Create djando App with command : python manage.py startapp contacts

Create Database Migration with below commands:

python manage.py makemigrations contacts
python manage.py migrate

Run the server :
python manage.py runserver
