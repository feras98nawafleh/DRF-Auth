from django.shortcuts import render
from rest_framework import generics, permissions
from .serializers import PostSerialzer
from .models import Post
from .permissions import IsAuthenticatedOrReadOnly

# create your views here

class PostList(generics.ListCreateAPIView):
    # queryset = Post.objects.filter(published = True)
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
    permission_class = (IsAuthenticatedOrReadOnly,)
    

# RUD view
class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerialzer
    permission_class = (IsAuthenticatedOrReadOnly,)