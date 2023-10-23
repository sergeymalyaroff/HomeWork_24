from rest_framework import serializers
from .models import Course
from lessons_app.models import Lesson



class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'title', 'preview_image', 'description', 'lessons_count']


    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()
