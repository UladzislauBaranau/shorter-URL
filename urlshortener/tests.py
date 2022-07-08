from django.contrib.auth.models import User
from django.test import Client, TestCase
from django.urls import reverse

from .models import Urls


class RegisterTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.invalid_data = {
            'username': 'testuser1',
            'email': 'testemail1@gmail.com',
            'password1': 'testpass1',
            'password2': 'testpass11111111',
        }
        self.valid_data = {
            'username': 'testuser1',
            'email': 'testemail1@gmail.com',
            'password1': 'testpass1',
            'password2': 'testpass1',
        }

    def test_register_page_status_code(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'urlshortener/register.html')

    def test_register_user_fail(self):
        response = self.client.post(reverse('register'), self.invalid_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 0)

    def test_register_user_success(self):
        response = self.client.post(reverse('register'), self.valid_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)


class LoginShortenerTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            username='testuser1',
            email='testemail1@gmail.com',
        )
        self.user.set_password('testpass1')
        self.user.save()
        self.user.is_active = True
        self.test_url = 'https://docs.djangoproject.com/en/3.2/topics/testing/tools/'

    def test_login_page_status_code(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'urlshortener/login.html')

    def test_login_user_success(self):
        response = self.client.post(reverse('login'), {'username': 'testuser1', 'password': 'testpass1'})
        self.assertEqual(response.status_code, 302)

    def test_login_user_fail(self):
        response = self.client.post(reverse('login'), {'username': 'testuser1', 'password': 'testpass111111'})
        self.assertEqual(response.status_code, 200)

    def test_shortener_page_status_code(self):
        self.test_login_user_success()

        response = self.client.get(reverse('shortener'))
        self.assertEqual(response.status_code, 200)

    def test_shortener(self):
        self.test_login_user_success()
        self.assertEqual(Urls.objects.count(), 0)

        response = self.client.post(reverse('shortener'), {'origin_url': self.test_url})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Urls.objects.count(), 1)

    def test_links_page_status_code(self):
        self.test_login_user_success()

        response = self.client.get(reverse('links'))
        self.assertEqual(response.status_code, 200)
