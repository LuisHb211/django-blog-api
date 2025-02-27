from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponse
from .models import Blog
from .serializer import BlogSerializer

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework. response import Response
from django.contrib.auth import authenticate
from rest_framework import status


@api_view(['POST'])
def custom_auth_token(request):
  description = {
    'Api Login': 'token:'
  }
  
  username = request.data.get('username')
  password = request.data.get('password')
  user = authenticate(username=username, password=password)
  if user is not None:
    token, created = Token.objects.get_or_create(user=user)
    return Response({
      'token': token.key,
      'user_id': user.id, 
      'email': user.email
    })
  else:
    return Response({'error': 'Invalid Credentials!'}, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
  api_urls = {
    'Api token': 'api-token-auth/',
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
  serializer = BlogSerializer(blog, many = False)
  return Response(serializer.data)

@api_view(['POST'])
def blogCreate(request):
  serializer = BlogSerializer(data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)

@api_view(['POST'])
def blogUpdate(request, pk):
  blog = Blog.objects.get(id=pk)
  serializer = BlogSerializer(instance = blog, data = request.data)
  if serializer.is_valid():
    serializer.save()
  return Response(serializer.data)
  
@api_view(['DELETE'])
def blogDelete(request, pk):
  blog = Blog.objects.get(id=pk)
  blog.delete()
  return Response("Blog is succecssfuly delete!")