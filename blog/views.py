from django.shortcuts import get_object_or_404, render, redirect
from .models import Post

def home(request):
    posts = Post.objects.all().order_by('-created_at')  # все посты, сначала новые
    return render(request, 'blog/home.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    
# ❤️ Новая функция для лайков
def like_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.likes += 1  # увеличиваем счётчик на 1
    post.save()      # сохраняем в базу
    return redirect('post_detail', pk=pk)  # возвращаемся на страницу поста