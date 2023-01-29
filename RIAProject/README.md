## Setup (Assuming You're on windows)

Create a virtual environment named .venv
`py -m venv .venv`

Activate the virtual environment, to ensure all python packages are installed into the virtual environment, and not globally
`.venv\Scripts\activate.bat`

## Installation (Assuming You're on windows)

Install Django package into your virtual environment
`py -m pip install django`

## Usage

### Running

`py manage.py runserver`

### Accessing Admin View

Go to http://127.0.0.1:8000/admin

### Accessing Login

http://127.0.0.1:8000/users/accounts/login/

### Accessing Log Out

http://127.0.0.1:8000/users/accounts/logout/

### Accessing Password Reset

http://127.0.0.1:8000/users/accounts/password_reset/
Currently, this only works if the email address is actually associated with a user. A link will appear in the terminal output
