from django.db import models
from django.conf import settings
from .tasks import send_course_update_email  # Импорт задачи Celery

class CourseSubscription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='subscriptions')
    course = models.ForeignKey('Course', on_delete=models.CASCADE, related_name='subscribers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ['user', 'course']


class Course(models.Model):
    title = models.CharField(max_length=255)
    preview_image = models.ImageField(upload_to='course_previews/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        # Флаг, указывающий, является ли это новым курсом или обновлением существующего
        is_new = self._state.adding
        super().save(*args, **kwargs)

        # Если это обновление курса, отправляем уведомления
        if not is_new:
            subscribers = self.subscribers.all()
            for subscription in subscribers:
                send_course_update_email.delay(subscription.user.email, self.title)


class Payment(models.Model):
    PAYMENT_METHODS = (
        ('cash', 'Наличные'),
        ('transfer', 'Перевод на счет')
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    payment_date = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=True)
    lesson = models.ForeignKey('lessons_app.Lesson', on_delete=models.SET_NULL, null=True, blank=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=8, choices=PAYMENT_METHODS)

    def __str__(self):
        return f"Payment by {self.user.email} on {self.payment_date}"
