# Scrum App
Sample Scrum App built in django 1.8.3+crispy-forms+bootstrap3

# Assumptions
You already have installed virtualenv and pip

# Functionalities
a. Allows user to register
b. Allows user to login
c. Allows user to create/edit sprints
d. Allows user to create/edit stories
e. Allows user to view scrum board for particular sprint
f. Allows user to create tasks for a story on scrum board
g. Allows user to assign/unassign task to himself
h. Restricts user from assigning/unassigning tasks not owned by him
i. Allows user to change the task status by drag n  drop on scrum board
j. Restricts user from changing tast status of unasinged or non-owned tasks
k. Dashboard gives user a consolidated view of tasks he/she owns that are in pipe, in progress and completed

# To install
a. clone the repo in your virtualenv folder
b. cd scrum_app
c. pip freeze -r requirements.txt
d. To run the app use command:
      python manage.py runserver --insecure
   We are running as insecure since settings.DEBUG is False.
e. To run the app in debug mode:
    - change DEBUG to True in scrum_app/settings.py
    - python manage.py runserver
    
