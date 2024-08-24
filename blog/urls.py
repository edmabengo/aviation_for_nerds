from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # La page d'accueil
    path('articles/', views.article_list, name='article_list'),
    path('', views.posts_list, name='posts_list'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('nerdy-challenges/', views.nerdy_challenges, name='nerdy_challenges'),  # Route pour "Nerdy Challenges"
]
