from rest_framework import viewsets, permissions, status
from .models import Post
from .serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
  queryset = Post.objects.all()
  permissions_classes = [permissions.AllowAny]
  serializer_class = PostSerializer