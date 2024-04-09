
celery_app.conf.beat_schedule = {
    # executes at sunset in intanbul
    'lower_shades_at_sunset': {
        'task': 'tasks.lower_shades_completely',
        'schedule': solar('sunset', 41.0082, 28.9784),
    },
}