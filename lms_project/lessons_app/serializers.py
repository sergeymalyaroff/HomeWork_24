#lessons_app/serializers.py

from rest_framework import serializers
from lessons_app.models import Lesson
import re

# Функция валидации одной ссылки
def validate_youtube_url(url):
    # Проверка на соответствие паттерну YouTube URL
    if not re.match(r'^(https?://)?(www\.)?(youtube\.com|youtu\.?be)/.+$', url):
        raise serializers.ValidationError("Неверная ссылка на видео. Допустимы только ссылки на YouTube.")
    return url

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'title', 'description', 'preview_image', 'video_link']

    def validate_video_link(self, value):
        # Проверяем ссылку на видео
        return validate_youtube_url(value)
