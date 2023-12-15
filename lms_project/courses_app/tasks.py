#lms_project/courses_app/tasks.py

from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_course_update_email(user_email, course_title):
    send_mail(
        'Обновление курса',
        f'Курс {course_title} был обновлен.',
        'from@example.com',
        [user_email],
        fail_silently=False,
    )
