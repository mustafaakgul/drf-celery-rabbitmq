CELERY_IMPORTS = ('tasks')
CELERY_IGNORE_RESULT = False
BROKER_HOST = '127.0.0.1'
BROKER_PORT = 5672
BROKER_URL = 'amqp://' #guest:guest@localhost:5672//

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'doctor-every-10-seconds': {
        'task': 'tasks.fav_doctor',
        'schedule': timedelta(seconds=10),
    },
}