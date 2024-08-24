from django.shortcuts import render, get_object_or_404
from .models import Post  # Importe ton modèle d'article

def article_list(request):
    posts = Post.objects.all()  # Récupère tous les articles
    return render(request, 'articles.html', {'posts': posts})

def home(request):
    return render(request, 'home.html')  # Assure-toi que 'home.html' est le bon fichier de template

# Mise à jour de la vue "posts_list"
def posts_list(request):
    posts = Post.objects.all()  # Récupère tous les articles
    return render(request, 'posts_list.html', {'posts': posts})  # Passe les articles au template

def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    return render(request, 'post_detail.html', {'post': post})

def nerdy_challenges(request):
    return render(request, 'nerdy_challenges.html')  # Utilise un template nommé nerdy_challenges.html
