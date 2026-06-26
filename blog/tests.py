from django.test import TestCase
from django.urls import reverse
from .models import Post

class PostModelTest(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(
            title="Тест",
            content="Тестовый контент"
        )
        self.assertEqual(post.title, "Тест")

class LikeTest(TestCase):
    def test_like_increases(self):
        post = Post.objects.create(title="Пост для лайка", content="...")
        self.assertEqual(post.likes, 0)
        
        response = self.client.post(reverse('like_post', args=[post.pk]))
        self.assertEqual(response.status_code, 302)  # редирект после лайка
        
        post.refresh_from_db()
        self.assertEqual(post.likes, 1)