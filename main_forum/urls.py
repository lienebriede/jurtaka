from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/', views.post_create, name='post_create'),
    path('search/', views.search_results, name='search_results'),
    path('<slug:slug>/', views.post_detail, name = 'post_detail'),
    path('<slug:slug>/edit_post/<int:post_id>/', views.post_edit, name='post_edit'),
    path('<slug:slug>/delete_post/<int:post_id>/', views.post_delete, name='post_delete'),
    path('<slug:slug>/like/', views.like_post, name='like_post'),
]
