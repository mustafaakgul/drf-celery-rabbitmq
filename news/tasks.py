from celery import shared_task
from django.core.mail import send_mail

from news.models import Issue, Subscription
import string

from django.contrib.auth.models import User
from django.utils.crypto import get_random_string


@shared_task()
def send_issue(issue_id):
    issue = Issue.objects.get(pk=issue_id)
    for subscription in Subscription.objects.filter(newsletter=issue.newsletter):
        send_email.delay(subscription.subscriber.email, issue.title, issue.content)


@shared_task()
def send_email(email, title, content):
    send_mail(
        title,
        content,
        'mustafaakguldev@gmail.com',
        [email],
        fail_silently=False,
    )


@shared_task
def add(x, y):
    return x + y


@shared_task
def create_random_user_accounts(total):
    for i in range(total):
        username = 'user_{}'.format(get_random_string(10, string.ascii_letters))
        email = '{}@example.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return '{} random users created with success!'.format(total)