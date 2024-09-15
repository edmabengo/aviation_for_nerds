from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone
from django.http import HttpResponse
from .models import UserExperience
from .forms import UserExperienceForm

def article_list(request):
    posts = Post.objects.all()
    return render(request, 'articles.html', {'posts': posts})

def home(request):
    return render(request, 'home.html')

def posts_list(request):
    posts = Post.objects.all()  # Fetch all posts, regardless of publish_date
    return render(request, 'posts_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.publish_date > timezone.now():
        return HttpResponse("This post will be available on its publication date.", status=403)
    return render(request, 'post_detail.html', {'post': post})

def nerdy_challenges(request):
    return render(request, 'nerdy_challenges.html')  # Utilise un template nommé nerdy_challenges.html
