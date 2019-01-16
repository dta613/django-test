# Pre-production environment for testing deployment
#This is a test environment for Django.

# Setup Instructions

## Requirements

You must install these prior to proceeding to the next steps. This can differ
depending on which Operating System your system is using.

- Python
- Pip
- Django

## Install Dependencies

Run this command (you may need to prepend with sudo in-case your current user does not have permission)
```
pip install -r pip-requirements.txt
pip install -r requirements.txt
```

## Setup Environment

1. Create a file `.env` in the root directory
2. Add `SECRET_KEY=[insert_random_string]`
3. Add `DEBUG=True`

Your file should look a like this:
```
SECRET_KEY=pokopwkeopfkweofkwpoekfopwkef
DEBUG=True
```

## Create Postgres Database

1. Install postgres
2. Enter the interactive shell provided by postgres.
```
psql postgres
```
3. Create the database using this command (replace database_name)
```
CREATE DATABASE [database_name];
```
4. Add `DATABASE_URL=postgres://localhost:5432/[database_name]` to the .env file 

## Run Migrations

Execute the following code in the root directory to ensure migrations are applied to your database
```
python manage.py migrate
```

## Start Server

1. Execute this in your root directory
```
python manage.py runserver
```
2. Navigate to `http://localhost:8000/` in your browser to access application

