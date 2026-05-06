1. mkdir project
2. cd project
3. python -m venv venv
4. activate venv
5. pip install django
6. django-admin startproject config .
7. python manage.py startapp core
8. add app in settings.py
9. pip freeze > requirements.txt
10. write code
11. python manage.py runserver