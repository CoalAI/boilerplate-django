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
    ./setup.sh
```
<br/> make sure to update the contents of the .env file that is generated in setup 1
<br/>
``` 
python3 manage.py makemigrations 
python3 manage.py migrate 
```
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
```python3 manage.py runserver```
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
```gunicorn project.wsgi -b 0.0.0.0:8000```

