from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Post
# Create your tests here.

class Blogtest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username = "username",
            email = "test@test.com",
            password = "secret",
        )

        cls.post = Post.objects.create(
            author = cls.user,
            title = "A good post",
            body = "Nice body content",
        )

    def test_post_model(self):
        self.assertEqual(self.post.author.username, "username")
        self.assertEqual(self.post.title, "A good post")
        self.assertEqual(self.post.body, "Nice body content")
        self.assertEqual(str(self.post), "A good post")