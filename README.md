Pre-production environment for testing deployment

This is a test environment for Django.

### Functionality being tested include:
- REST API
- Admin page
- App for user authentication
- CRUD for data
- Heroku deployment

### To test, please following these steps:

Either clone and download the project, and go to the command-line for the next steps.

Use a virtual environment to separate the package versions for this Django application from your other projects

### Run the following code:

```
virtualenv my_project
source my_project/bin/activate

```

Using the virtual environment allows you to install the package requirements in a controlled environment.

### Use the following code to gather the required libraries for running this project:

```
pip install requirements.txt
```

After installing all the project, you can now start launching Django as an web application server.

Go to the directory in which ```manage.py``` is located.

### Go ahead, run the command:

```python manage.py runserver```

You should be able to see the server running in ```localhost:8000```

Congratulations! Happy hacking!
