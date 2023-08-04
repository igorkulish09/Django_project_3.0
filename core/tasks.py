from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_mail_to_admins(name, email, message):
    subject = f'New Contact Form Submission from {name}'
    body = f'Name: {name}\nEmail: {email}\nMessage: {message}'
    from_email = 'noreply@example.com'
    to_emails = ['admin1@example.com', 'admin2@example.com']
    send_mail(subject, body, from_email, to_emails)
