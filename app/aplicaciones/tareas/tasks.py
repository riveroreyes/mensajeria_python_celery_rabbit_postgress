from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User
from app import settings
import time

@shared_task
def send_emails_user():
    asunto = 'Mensaje de prueba' 
    mensaje = 'Bienvenido, este es un mensaje de prueba CELERY, RABBITMQ Y DJANGO'
    users = User.objects.all()
    for user in users:
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
        time.sleep(1)

    return '{} Se envio el correo correctamente'.format(user)