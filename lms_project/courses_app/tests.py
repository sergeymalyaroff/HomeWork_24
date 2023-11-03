# lms_project/courses_app/tests.py

from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from courses_app.models import Course, Subscription
from lessons_app.models import Lesson

class LessonTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
        self.course = Course.objects.create(title="Test Course", description="Test Course Description")
        self.lesson = Lesson.objects.create(title="Test Lesson", description="Test Lesson Description", course=self.course)

    def test_create_lesson(self):
        url = reverse('lesson-list-create')
        data = {'title': 'New Lesson', 'description': 'New Lesson Description', 'course': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_lesson(self):
        url = reverse('lesson-detail-update-delete', args=[self.lesson.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_lesson(self):
        url = reverse('lesson-detail-update-delete', args=[self.lesson.id])
        data = {'title': 'Updated Lesson', 'description': 'Updated Lesson Description', 'course': self.course.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_lesson(self):
        url = reverse('lesson-detail-update-delete', args=[self.lesson.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

class SubscriptionTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token.key)
        self.course = Course.objects.create(title="Test Course", description="Test Course Description")

    def test_subscribe_course(self):
        url = reverse('course-subscription-list')
        data = {'course': self.course.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_unsubscribe_course(self):
        self.test_subscribe_course()
        subscription = Subscription.objects.get(course=self.course, user=self.user)
        url = reverse('course-subscription-detail', args=[subscription.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
