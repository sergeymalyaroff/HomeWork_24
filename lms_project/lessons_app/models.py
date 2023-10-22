from django.db import models

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    preview_image = models.ImageField(upload_to='lesson_previews/', null=True, blank=True)
    video_link = models.URLField()

    def __str__(self):
        return self.title
