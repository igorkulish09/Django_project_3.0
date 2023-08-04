from django.core.mail import EmailMessage
from django.conf import settings


def send_mail_to_admins(subject, message, from_email=None, **kwargs):
    if from_email is None:
        from_email = settings.DEFAULT_FROM_EMAIL

    mail_subject = subject
    mail_message = message

    for admin_email in [admin_email[1] for admin_email in settings.ADMINS]:
        email = EmailMessage(mail_subject, mail_message, from_email, [admin_email], **kwargs)
        email.send()

# Приклад використання
subject = 'Новий коментар на сайті'
message = 'На сайті з\'явився новий коментар. Перевірте адміністративний розділ для його перегляду.'

send_mail_to_admins(subject, message)
