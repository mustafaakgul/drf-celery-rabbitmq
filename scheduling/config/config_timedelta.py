from celery import Celery

celery_app.conf.beat_schedule = {
    'process_likes': {
        'task': 'tasks.process_likes',
        'schedule': 30
    },
}
celery_app.conf.timezone = 'UTC'

# periodic work at every 30 seconds
# more clear way to do send order to rabbitmq(write to db) at every 30 seconds
# if worker is available at that time task will be executed immediately
# if worker is not available at that time task will be work in uncertain time
# in turkish : 30 sn de bir iş emri yarat