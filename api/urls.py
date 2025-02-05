from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='home'),
    path('blog-list/', views.blogList, name='blog-list'),
    path('blog-list/<str:pk>/', views.blogDetail, name='blog-detail'),
]