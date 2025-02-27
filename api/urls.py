from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='home'),
    path('blog-list/', views.blogList, name='blog-list'),
    path('blog-detail/<str:pk>/', views.blogDetail, name='blog-detail'),
    path('blog-create/', views.blogCreate, name='blog-create'),
    path('blog-update/<str:pk>/', views.blogUpdate, name='blog-update'),
    path('blog-delete/<str:pk>/', views.blogDelete, name='blog-delete'),
    path('api-token-auth/', views.custom_auth_token),
]