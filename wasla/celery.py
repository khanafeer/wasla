import os

from celery import Celery

from wasla import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'wasla.settings')

app = Celery('wasla')
app.config_from_object(lambda: settings.INSTALLED_APPS)

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'section_1': {
        'task': 'posts_viewer.tasks.get_news',
        'schedule': 60.0,
        'args': ('sports',)
    }, 'section_2': {
        'task': 'posts_viewer.tasks.get_news',
        'schedule': 60.0,
        'args': ('science',)

    }, 'section_3': {
        'task': 'posts_viewer.tasks.get_news',
        'schedule': 60.0,
        'args': ('politics',)

    }, 'section_4': {
        'task': 'posts_viewer.tasks.get_news',
        'schedule': 60.0,
        'args': ('movies',)
    },
}
