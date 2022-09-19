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
  ENGINE="django.db.backends.postgresql"
  NAME="mydatabase"
  USER="mydatabaseuser"
  PASSWORD="mypassword"
  HOST="127.0.0.1"
  PORT="5432"
```


## Development
set DEBUG = 1 in **.env**
#### Running the project
```python3 manage.py runserver```



## Production
#### Running the project
```python3 manage.py runserver```
#### Deployment
