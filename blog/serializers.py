from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = ('id', 'title', 'first_text', 'second_text', 'third_text', 'fourth_text', 'five_text')
    read_only_fields = ('id', 'title')