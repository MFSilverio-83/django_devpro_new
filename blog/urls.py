from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'), # página inicial
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'), # exibição de um post específico
    path('post/new/', views.post_new, name='post_new'), # criação de um novo post
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('drafts/', views.post_draft_list, name='post_draft_list'), # rascunho antes de salvar
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
]
