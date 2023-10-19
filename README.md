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


### Email Verify Endpoints
The following endpoints are provided:  
1. POST api/signup/ - signs up user and send email verification
2. POST api/signup/verify - it takes code and verify user. Email is sent with this link. User clicks on this link and user's email is verified.  


### Password Reset Endpoints
The following endpoints are provided:  
1. POST api/password/reset - sends email to user for password reset. Email has link for password reset page and code to reset password. You have to add reset link in env file as given in env-sample.
2. POST api/password/reset/verified - takes new password and code (sent via email) and updates password


### Password Change Endpoint  
1. POST api/password/change/ - it is only allowed for logged in users. It takes new password and updates it.


### Login/Signup through Google
1. api/google-login/ - shows signup/login through google screen and redirects to your frontend home page if login/signup is succssfull.  
You need to add LOGIN_REDIRECT_URL, FRONTEND_REDIRECT_URL, SOCIAL_AUTH_GOOGLE_OAUTH2_KEY and SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET in your .env file. Follow <a href="https://theonetechnologies.com/blog/post/how-to-get-google-app-client-id-and-client-secret">this</a> tutorial to generate Client ID and Client Secret. LOGIN_REDIRECT_URL will be **BASE_URL_OF_DJANGO_APP/api/google-callback/** and also add this in Authorized Redirect URIs when creating credentials.


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
```
If you have not configured your database for deployment then run this command to start containers:
```
docker-compose -f docker-compose-sql.yml up -d
```
otherwise:
```
docker-compose -f docker-compose.yml up -d
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
<li><a href="https://pypi.org/project/django-rest-authemail/">django-rest-authemail</a></li>
<li><a href="https://pypi.org/project/social-auth-app-django/#description">social-auth-app-django</a></li>
</ul>
