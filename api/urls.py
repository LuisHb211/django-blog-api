from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='home'),
    path('blog-list/', views.blogList, name='blog-list'),
]