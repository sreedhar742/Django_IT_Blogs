from celery import shared_task
from django.core.mail import send_mail
import logging

logger = logging.getLogger(__name__)

@shared_task()
def sending_email(message, subject, email_from, recipient_list):
    logger.info(f"Sending email with message={message}, subject={subject}, from={email_from}, to={recipient_list}")
    try:
        send_mail(subject, message, email_from, recipient_list)
    except Exception as e:
        logger.error(f"Error sending email: {e}")

