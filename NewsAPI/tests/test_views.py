from .test_setup import TestSetUp
from scraping.models import News
from ..serializers import NewsSerializer

from django.test import TestCase
from scraping.tasks import financialnews_rss

class TestViews(TestSetUp):

    def test_task_no_error(self):
        result = financialnews_rss()
        news = News.objects.all()
        self.assertTrue(len(news) > 0)

    def test_user_successfully_login_with_correct_credentials(self):
        res = self.client.post(self.login_url, self.user_data, format="json")
        self.assertEqual(res.status_code, 200)

    def test_news_page_loaded(self):
        result = financialnews_rss()
        res = self.client.get(self.news_results_per_page_url, {}, True)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.data["results"]), 10)

    def test_news_detail(self):
        result = financialnews_rss()
        res = self.client.get(self.news_details, format='json')
        self.assertIsNotNone(res)