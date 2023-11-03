#lms_project/courses_app/vievs.py

from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer
from .models import Payment
from .serializers import PaymentSerializer
from .filters import PaymentFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.permissions import BasePermission
from rest_framework import status, viewsets
from rest_framework.response import Response
from .models import CourseSubscription
from .serializers import CourseSubscriptionSerializer

class CourseSubscriptionViewSet(viewsets.ModelViewSet):
    queryset = CourseSubscription.objects.all()
    serializer_class = CourseSubscriptionSerializer

    def create(self, request, *args, **kwargs):
        # Здесь нужна логика проверки, что пользователь не подписан на курс
        return super().create(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        # Здесь нужна логика проверки, что подписка существует
        return super().destroy(request, *args, **kwargs)

class IsOwnerOrModerator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user == obj.user or request.user.groups.filter(name='Moderators').exists()

class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.groups.filter(name='Moderators').exists()

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated, IsOwnerOrModerator)


class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_class = PaymentFilter
    permission_classes = (IsAuthenticated, IsOwnerOrModerator,)
