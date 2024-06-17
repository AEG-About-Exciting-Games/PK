from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(email='test@test.com', password='password123', nickname='testuser')

    def test_signup_view(self):
        response = self.client.get(reverse('users:signup'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('users:signup'), {
            'email': 'newuser@example.com',
            'nickname': 'newuser',
            'password1': 'newpassword123',
            'password2': 'newpassword123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(email='newuser@example.com').exists())

    # def test_login_view(self):
    #     response = self.client.get(reverse('users:login'))
    #     self.assertEqual(response.status_code, 200)
    #
    #     response = self.client.post(reverse('users:login'), {
    #         'username': 'test@example.com',
    #         'password': 'password123'
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.assertEqual(int(self.client.session['_auth_user_id']), self.user.pk)
    #
    def test_logout_view(self):
        self.client.login(email='tes1t@test.com', password='djangotest1')
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)
        self.assertNotIn('_auth_user_id', self.client.session)

    # def test_update_view(self):
    #     self.client.login(email='tes1t@test.com', password='djangotest1')
    #     response = self.client.get(reverse('users:update'))
    #     self.assertEqual(response.status_code, 200)
    #
    #     response = self.client.post(reverse('users:update'), {
    #         'email': 'update@example.com',
    #         'nickname': 'updateduser'
    #     })
    #     self.assertEqual(response.status_code, 302)
    #     self.user.refresh_from_db()
    #     self.assertEqual(self.user.email, 'update@example.com')
    #     self.assertEqual(self.user.nickname, 'updateduser')

    # def test_unsubscribe_view(self):
    #     self.client.login(email='test@example.com', password='password123')
    #     response = self.client.get(reverse('users:unsubscribe'))
    #     self.assertEqual(response.status_code, 200)
    #
    #     response = self.client.post(reverse('users:unsubscribe'))
    #     self.assertEqual(response.status_code, 302)
    #     self.assertFalse(User.objects.filter(email='test@example.com').exists())
