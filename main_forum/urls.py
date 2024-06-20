from . import views
from django.urls import path

urlpatterns = [
    path('', views.post_list, name='home'),
    path('post/', views.post_create, name='post_create'),
    path('<slug:slug>/', views.post_detail, name = 'post_detail'),
    path('<slug:slug>/edit_post/<int:post_id>/', views.post_edit, name='post_edit'),
]
