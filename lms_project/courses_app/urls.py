# lms_project/courses_app/urls.py

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CourseViewSet, CourseSubscriptionViewSet

router = DefaultRouter()
router.register(r'courses', CourseViewSet)
router.register(r'subscriptions', CourseSubscriptionViewSet, basename='course-subscription')

urlpatterns = [
    path('', include(router.urls)),  # Включаем все зарегистрированные маршруты одним вызовом
    path('create-payment-intent/', CreatePaymentIntentView.as_view(), name='create-payment-intent'),
    path('retrieve-payment-intent/', RetrievePaymentIntentView.as_view(), name='retrieve-payment-intent'),

]
