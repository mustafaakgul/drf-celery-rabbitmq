## Practice Django, Celery, and RabbitMQ integration with this project repository

```
from celery import Celery
app = Celery('tasks', broker='pyamqp://guest@localhost//')
@app.task
def add(x, y):
    return x + y
# Can be run worker by executing the following command: celery -A tasks worker --loglevel=INFO
```

### Short Commands
 * celery worker --help
 * celery help


### docker-compose up
### python manage.py makemigrations
### Run Celery: celery -A newsletter_site worker --loglevel=INFO



#### Run the Project
* Run docker-compose to start the dependencies: docker-compose up
* Generate migrations for our models: python manage.py makemigrations
* To apply generated migrations to database run: python manage.py migrate
* To create a user for login run the following command and provide your details: python manage.py createsuperuser
* Run the following command to run the app and open http://127.0.0.1:8000/admin to open Django Admin : python manage.py runserver
* Run celery: celery -A drf_celery_rabbitmq worker --loglevel=INFO
