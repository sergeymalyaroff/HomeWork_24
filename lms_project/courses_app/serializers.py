#lms_project/courses_app/serializers.py

from .models import Course
from lessons_app.serializers import LessonSerializer
from lessons_app.models import Lesson
from rest_framework import serializers
from .models import Payment

class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    class Meta:
        model = Course
        fields = ['id', 'title', 'preview_image', 'description', 'lessons_count', 'lessons']

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'