#lms_project/users_app/admin.py

from django.contrib import admin
from .models import CustomUser

admin.site.register(CustomUser)



