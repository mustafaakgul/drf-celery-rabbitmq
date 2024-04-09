
celery_app.conf.beat_schedule = {
    # executes every friday afternoon at 5:30 pm.
    'send_weekly_digest': {
        'task': 'tasks.send_weekly_digest',
        'schedule': crontab(hours=17, minute=30, day_of_week=5),
    },
}