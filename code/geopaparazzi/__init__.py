import os
from .celery import celery_app

#__all__ = ('celery_app',)

default_app_config = "geopaparazzi.apps.AppConfig"


def main(global_settings, **settings):
    from django.core.wsgi import get_wsgi_application
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings.get('django_settings'))
    app = get_wsgi_application()
    return app
