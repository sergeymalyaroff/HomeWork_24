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
import stripe
from django.conf import settings
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

stripe.api_key = settings.STRIPE_SECRET_KEY

class CreatePaymentIntentView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            # Создаем платежный интент
            intent = stripe.PaymentIntent.create(
                amount=request.data.get("amount"),  # Сумма в центах
                currency='usd',  # Валюта
                payment_method_types=['card'],  # Методы оплаты
            )
            return Response({"client_secret": intent.client_secret}, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)

class RetrievePaymentIntentView(APIView):
    def get(self, request, *args, **kwargs):
        try:
            # Получаем платежный интент по ID
            intent = stripe.PaymentIntent.retrieve(request.data.get("intent_id"))
            return Response({"payment_intent": intent}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


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
