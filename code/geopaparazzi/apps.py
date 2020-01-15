from django.apps import AppConfig as BaseAppConfig


def run_setup_hooks(*args, **kwargs):
    from django.conf import settings
    from .celery import celery_app
    if celery_app not in settings.INSTALLED_APPS:
        settings.INSTALLED_APPS += (celery_app, )


class AppConfig(BaseAppConfig):

    name = "geopaparazzi"
    label = "geopaparazzi"

    def ready(self):
        super(AppConfig, self).ready()
        run_setup_hooks()
