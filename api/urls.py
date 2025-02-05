from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='home'),
    path('blog-list/', views.blogList, name='blog-list'),
    path('blog-detail/<str:pk>/', views.blogDetail, name='blog-detail'),
    path('blog-create/', views.blogCreate, name='blog-create'),
]