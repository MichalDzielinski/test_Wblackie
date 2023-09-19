from django.test import TestCase
from .models import Post
from http import HTTPStatus

class PostModelTest(TestCase):
    def test_post_model_exists(self):
        posts = Post.objects.count()

        self.assertEqual(posts,0 )

    def test_string_rep_of_objects(self):
        post = Post.objects.create(
            title='Test Post',
            body ='Test body',
        )

        self.assertEqual(str(post), post.title)

class HomepageTest(TestCase):
    def setUp(self):
        Post.objects.create(
            title='sample post 1',
            body ='some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text',
        )
        Post.objects.create(
            title='sample post 2',
            body ='some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text some text',
        )

    def test_homepage_returns_correct_response(self):
        response = self.client.get('/')

        self.assertTemplateUsed(response, 'posts/index.html')
        self.assertEqual(response.status_code, HTTPStatus.OK )