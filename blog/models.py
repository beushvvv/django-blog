from django.db import models

class Post(models.Model):
    # Поле для заголовка — строка, максимум 200 символов
    title = models.CharField(max_length=200)
    # Поле для текста — большое текстовое поле
    content = models.TextField()
    # Поле для даты создания — автоматически заполняется текущей датой
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    # Это метод для красивого отображения поста в админке
    def __str__(self):
        return self.title
