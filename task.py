from celery import Celery
from time import sleep

app = Celery('tasks', broker='amqp://127.0.0.1', backend='db+sqlite:///db.sqlite3')

@app.task
def reverse(text):
    sleep(5) # simulating long running task
    return text[::-1]

# to run this func in python console in ide
# from tasks import reverse
# reverse('hello')

# In terminal
# celery -A tasks worker --loglevel=info
# see this rabbitmq is running
# on the other tab in the terminal, run this command
# from tasks import reverse
# reverse.delay('hello')
# and look other terminal in running rabbitmq and see result

# start again console in ide second tab
# python3
# from tasks import reverse
# result = reverse.delay('hellomustafa)
# result
# result.status
# a few seconds later result.status will be 'SUCCESS'
# result.get()
# again result = reverse.delay('hellomustafa')
# write immediately result.get() and program will wait you for second result for queue
# and browse the database to see the result