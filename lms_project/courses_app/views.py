from rest_framework import viewsets
from .models import Course
from .serializers import CourseSerializer
from .models import Payment
from .serializers import PaymentSerializer
from .filters import PaymentFilter

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer




class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filterset_class = PaymentFilter
