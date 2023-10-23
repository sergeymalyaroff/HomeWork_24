from .models import Course
from lessons_app.serializers import LessonSerializer
from lessons_app.models import Lesson

class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True, source='lesson_set')

    class Meta:
        model = Course
        fields = ['id', 'title', 'preview_image', 'description', 'lessons_count', 'lessons']

    def get_lessons_count(self, obj):
        return Lesson.objects.filter(course=obj).count()
