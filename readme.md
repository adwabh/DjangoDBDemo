Section 7
============================
Lecture 31:
1. Customizing filtering
2. searching
3. Sorting capabilities


1. Configuring throttling policies
2. Testing throttling policies
3. Understanding filtering, searching and ordering classes
4. Configuring filtering, searching and ordering for views
5. Testing filtering, searching and ordering

Section 6
============================
Lecture 26:
Configured permission policies

Lecture 25:
1. Customizing permission class
2. Listing all users
3. Retrieving details for single user

Summary
============================

1. Designed RESTFul API to Interact with simple SQLite database
2. Defined requirements for our API
3. Set up a virtual environment with Django REST Framework
4. Created model to represent and persist game information
5. Executed migrations in Django
6. Managed serialization and de-serialization of game instances

Steps for Generating requirements.txt
======================================
1. pip freeze > requirements.txt

Steps for Testing
==================
1. python manage.py test -v 2
2. coverage report -m
3. coverage html

Steps for creating a 'postgres' database
=========================================
1. psql -U postgres
2. create database <NAME_OF_DATABASE>

Creating a user in postgres
============================
1. create role <NAME_OF_USER> with login password '<PASSWORD_FOR_USER>';
2. to list users : use command '\du'
3. to grant privileges to user 'grant all privileges on database games to test1;'
4. Use '\l' to verify privileges

Steps for Migrations
=====================
1. python <SOURCE>/Scripts/<PROJECT_NAME>/manage.py makemigrations
2. python <SOURCE>/Scripts/<PROJECT_NAME>/manage.py migrate
3. to check tables use 'psql --username=test1 --dbname=games --command="\dt"'

Steps for initializing Django Project
=====================================

1. Create Folder
2. Navigate to folder in command prompt/terminal
3. Create virtual environment with the command 'python -m venv'
4. Navigate to <Path/><Folder>/Scripts created in step 3 above
5. Execute activate/activate.bat to start virtual environment
6. Execute command 'pip install django' to install django
7. Execute command 'pip install djangorestframework' to install Django REST framework
8. Execute command 'python <Path/><Folder>/Scripts/django-admin.py startproject <NAME_OF_PROJECT_HERE>'
9. Navigate to the <NAME_OF_PROJECT> folder generated in step 9
10. Execute command 'python manage.py startapp <NAME_OF_APP>' this will create <NAME_OF_PROJECT>/<NAME_OF_APP> and rest of framework files and folders
