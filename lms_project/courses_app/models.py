from django.db import models


class Course(models.Model):
    title = models.CharField(max_length=255)
    preview_image = models.ImageField(upload_to='course_previews/', null=True, blank=True)
    description = models.TextField()

    def __str__(self):
        return self.title



