from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .models import Tweet

User = get_user_model()
class TweetModelTestCase(TestCase):
    def setUp(self):
        some_random_user = User.objects.create(username = 'dimi')
          

    def test_tweet_item(self):
        obj = Tweet.objects.create(
            user= User.objects.first(), 
            content='random models'
        )

        self.assertTrue(obj.content == 'random models')
        self.assertTrue(obj.id == 1)
        absolute_url = reverse("tweet:detail", kwargs={"pk":1})
        self.assertEqual(obj.get_absolute_url(),absolute_url)
