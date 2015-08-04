# Scrum App
Sample Scrum App built in django 1.8.3+crispy-forms+bootstrap3

# Assumptions
You already have installed virtualenv and pip

# Functionalities
* Allows user to register
* Allows user to login
* Allows user to create/edit sprints
* Allows user to create/edit stories
* Allows user to view scrum board for particular sprint
* Allows user to create tasks for a story on scrum board
* Allows user to assign/unassign task to himself
* Restricts user from assigning/unassigning tasks not owned by him
* Allows user to change the task status by drag n  drop on scrum board
* Restricts user from changing tast status of unasinged or non-owned tasks
* Dashboard gives user a consolidated view of tasks he/she owns that are in pipe, in progress and completed

# To install
* clone the repo in your virtualenv folder
* cd scrum_app
* Install the requirements 
```
pip freeze -r requirements.txt
```
* To run the app use command:
      ```python manage.py runserver --insecure```
   We are running as insecure since ```settings.DEBUG``` is False.
* To run the app in debug mode:
    - change DEBUG to True in scrum_app/settings.py
    - ```python manage.py runserver```
    
