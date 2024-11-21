from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'title', 'created_at', 'country', 'main_image', 'main_description', 'h1_title', 'h1_image', 'h2_title', 'h2_description', 'h2_image', 'h3_title', 'h3_description', 'h3_image', 'categories')
    read_only_fields = ('id', 'created_at', 'categories')