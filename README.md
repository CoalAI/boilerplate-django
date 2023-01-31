# boilerplate-django
This is Django boiler plate.


### Setup / Initialize the project
```
    python3 -m venv venv
```
```
    source venv/bin/activate
```
```
    sudo chown -R $USER:$USER .
    ./setup.sh
```
<br/> make sure to update the contents of the .env file that is generated in setup 1
<br/>
```
python3 manage.py makemigrations
python3 manage.py migrate
```

### Reset Password Endpoints
The following endpoints are provided:  
1. POST api/password_reset/ - request a reset password token by using the email parameter  
2. POST api/password_reset/confirm/ - using a valid token, the users password is set to the provided password  
3. POST api/password_reset/validate_token/ - will return a 200 if a given token is valid


#### Database
<br /> you may set the following variables inside **.env** file to configure any database
<br /> by **default** it uses **sqlite**
```
  DB_ENGINE="django.db.backends.postgresql"
  DB_NAME="mydatabase"
  DB_USER="mydatabaseuser"
  DB_PASSWORD="mypassword"
  DB_HOST="127.0.0.1"
  DB_PORT="5432"
```


## Development
set DEBUG = 1 in **.env**
#### Running the project
```
python3 manage.py runserver
```
#### Deployment
```
cp deploy/dev/* .
docker-compose up -d
```
to stop the containers:
```
docker-compose down
```


## Production
#### Running the project
```
gunicorn project.wsgi -b 0.0.0.0:8000
```


## Testing

the testing is based on **pytest** library
<br />  the **tests** directory holds all the test files
<br />  for a reference you can see **tests/api/test_sample.py**
<br />  for adding / editing the pytest configuration there is pytest.ini file in root directory
<br />  most importantly there is a package **pytest-dotenv** which allows you to define your
<br />  test environemnt variables seprately in **.test.env** file (especially the database config)


## Links
<ul>
<li><a href="https://docs.docker.com/samples/django/">django docker guide</a></li>
<li><a href="https://www.django-rest-framework.org/">django rest documentation</a></li>
<li><a href="https://www.djangoproject.com/">django core documentation</a></li>
<li><a href="https://github.com/dimaka-wix/commit-msg-hook">commit-msg</a></li>
<li><a href="https://pre-commit.com/hooks.html" >pre-commit supported hooks</a></li>
<li><a href="https://pytest-django.readthedocs.io/en/latest/database.html">pytest</a></li>
<li><a href="https://github.com/quiqua/pytest-dotenv">pytest-dotenv</a></li>
<li><a href="https://pypi.org/project/django-rest-passwordreset/">django-rest-passwordreset</a></li>
</ul>
