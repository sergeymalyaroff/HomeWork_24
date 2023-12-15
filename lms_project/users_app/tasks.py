#users_app/tasks.py


from celery import shared_task
from django.utils import timezone
from datetime import timedelta
from .models import CustomUser

@shared_task
def deactivate_inactive_users():
    one_month_ago = timezone.now() - timedelta(days=30)
    inactive_users = CustomUser.objects.filter(last_login__lt=one_month_ago, is_active=True)
    inactive_users.update(is_active=False)
