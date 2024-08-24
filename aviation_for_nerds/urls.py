"""
URL configuration for aviation_for_nerds project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from blog import views  # Assure-toi d'importer les vues de ton application blog
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),  # Chemin pour la page d'accueil
    path('articles/', views.article_list, name='article_list'),  # Chemin pour les articles
    path('posts/', views.posts_list, name='posts_list'),  # Chemin pour la page "Posts"
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),  # Chemin pour le détail d'un article
    path('nerdy-challenges/', views.nerdy_challenges, name='nerdy_challenges'),  # Chemin pour les "Nerdy Challenges"
]

if settings.DEBUG:  # Ajoute cette partie pour servir les fichiers media en développement
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




