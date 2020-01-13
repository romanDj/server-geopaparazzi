from django.conf import settings
from django.core.mail import get_connection, EmailMessage
from django.template.loader import render_to_string
from django.utils.translation import ugettext

from pinax.notifications.backends.base import BaseBackend


class EmailBackend(BaseBackend):
    spam_sensitivity = 2

    def can_send(self, user, notice_type, scoping):
        can_send = super(EmailBackend, self).can_send(user, notice_type, scoping)
        if can_send and user.email:
            return True
        return False

    def deliver(self, recipient, sender, notice_type, extra_context):
        # TODO: require this to be passed in extra_context
        connection = get_connection()

        # Manually open the connection
        connection.open()

        try:
            context = self.default_context()
            context.update({
                "recipient": recipient,
                "sender": sender,
                "notice": ugettext(notice_type.display),
            })
            context.update(extra_context)

            messages = self.get_formatted_messages((
                "short.txt",
                "full.txt"
            ), notice_type.label, context)

            context.update({
                "message": messages["short.txt"],
            })
            subject = "".join(render_to_string("pinax/notifications/email_subject.txt", context).splitlines())

            context.update({
                "message": messages["full.txt"]
            })
            body = render_to_string("pinax/notifications/email_body.txt", context)

            email = EmailMessage(
                subject=subject,
                body=body,
                from_email=settings.DEFAULT_FROM_EMAIL,
                to=[recipient.email, ],
                reply_to=[settings.DEFAULT_FROM_EMAIL, ])
            email.content_subtype = "html"

            connection.send_messages([email, ])
            # The connection was already open so send_messages() doesn't close it.
        except BaseException:
            pass
        finally:
            # We need to manually close the connection.
            connection.close()
