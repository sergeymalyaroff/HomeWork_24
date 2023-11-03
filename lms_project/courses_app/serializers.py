#lms_project/courses_app/serializers.py

from .models import Course
from lessons_app.serializers import LessonSerializer
from lessons_app.models import Lesson
from rest_framework import serializers
from .models import Payment
import re
from .models import CourseSubscription




class CourseSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseSubscription
        fields = ['id', 'user', 'course']

# Функция валидации ссылок
def validate_links(text):
    urls = re.findall(r'(https?://\S+)', text)
    for url in urls:
        if 'youtube.com' not in url:
            raise serializers.ValidationError("Ссылки на сторонние ресурсы запрещены, кроме youtube.com")
    return text

class CourseSerializer(serializers.ModelSerializer):
    is_subscribed = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'preview_image', 'description', 'lessons_count', 'lessons', 'is_subscribed']


    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()


    def validate_description(self, value):
        # Проверяем описание на наличие недопустимых ссылок
        return validate_links(value)

    def get_is_subscribed(self, obj):
        user = self.context['request'].user
        return CourseSubscription.objects.filter(user=user, course=obj).exists()

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'