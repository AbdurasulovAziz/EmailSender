import os


from django.core.mail import EmailMessage
from celery import Celery


# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmailSender.settings')

app = Celery('EmailSender')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task
def send_email(title: str, text:str, mail_list: list):

    email = EmailMessage(subject=title, body=text, to=mail_list)
    email.send()
