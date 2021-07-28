from django.urls import reverse
from django.test import TestCase, Client

class TestSetUp(TestCase):

    def setUp(self):
        # initialize the APIClient app
        self.client = Client()

        self.login_url = reverse('rest_framework:login')
        self.news_results_per_page_url = reverse('news-list')
        self.news_details = reverse('news-detail', args=['1'])

        self.user_data = {
            'email': "congo.naida@gmail.com",
            'username': "naidacongo",
            'password': "admin1234!"
        }

        return super().setUp()

    def tearDown(self):
        return super().tearDown