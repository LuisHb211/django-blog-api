from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Blog
from .serializer import BlogSerializer

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'List': 'api/blog-list/',
    'Detail View': 'api/blog-detail/<str:pk>/',
    'Create': 'api/blog-create/',
    'Update': 'api/blog-update/<str:pk>/',
    'Delete': 'api/blog-delete/<str:pk>/',
  }
  return Response(api_urls)

@api_view(['GET'])
def blogList(request):
  blog = Blog.objects.all()
  serializer = BlogSerializer(blog, many=True)
  return Response(serializer.data)

#In the blogDetail view, the many=False argument is used because this view is intended to handle a single Blog instance, not a list of instances.
@api_view(['GET'])
def blogDetail(request, pk):
  blog = Blog.objects.get(id=pk)
  serializer = BlogSerializer(blog, many=False)
  return Response(serializer.data)