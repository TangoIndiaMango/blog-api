from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.shortcuts import render
from .serializers import PostSerializer, UserSerializer
from .permissions import IsAuthOrReadOnly
from .models import Post
# Create your views here.




class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthOrReadOnly, )
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer




# from rest_framework import generics, permissions, 
# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthOrReadOnly, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthOrReadOnly, )
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

# #     permission_classes = (permissions.IsAdminUser, )

# class UserList(generics.ListCreateAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer

