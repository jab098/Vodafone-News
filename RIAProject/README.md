## Setup (Assuming You're on windows)

Create a virtual environment named .venv
`py -m venv .venv`

Activate the virtual environment, to ensure all python packages are installed into the virtual environment, and not globally
`.venv\Scripts\activate.bat`

## Installation (Assuming You're on windows)

Install Django package into your virtual environment
`py -m pip install django`

Install Crispy forms package into your virtual environment
`py -m pip install django-crispy-forms`

Install Django pwa to enable progressive web app (RIA) behaviour
`py -m pip install django-pwa`

## Usage

### Running

`py manage.py runserver`

### Creating admin user

`py manage.py createsuperuser`

### Creating end user

Please follow the front-end screens to do this

(You will need an end-user and admin user to be able to test all of the functionality)

### Accessing Admin View

Go to http://127.0.0.1:8000/admin

### Accessing Password Reset

http://127.0.0.1:8000/users/accounts/password_reset/
Currently, this only works if the email address is actually associated with a user. A link will appear in the terminal output
