from geopaparazzi.celery_app import app
from celery.utils.log import get_task_logger
from django.conf import settings
from django.core.mail import send_mail

logger = get_task_logger(__name__)


@app.task(bind=True,
          name='geopaparazzi.tasks.email.send_mail',
          queue='email',)
def send_email(self, *args, **kwargs):
    """
    Sends an email using django's send_mail functionality.
    """
    send_mail(*args, **kwargs)


@app.task(bind=True,
          name='geopaparazzi.tasks.notifications.send_queued_notifications',
          queue='email',)
def send_queued_notifications(self, *args):
    """Sends queued notifications.

    settings.PINAX_NOTIFICATIONS_QUEUE_ALL needs to be true in order to take
    advantage of this.

    """
    try:
        from notification.engine import send_all
    except ImportError:
        return

    # Make sure application can write to location where lock files are stored
    if not args and getattr(settings, 'NOTIFICATION_LOCK_LOCATION', None):
        send_all(settings.NOTIFICATION_LOCK_LOCATION)
    else:
        send_all(*args)
