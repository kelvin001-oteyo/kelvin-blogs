
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),  # 👈 NEW
    path('category/<str:category_name>/', views.posts_by_category, name='posts-by-category'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),



]
