from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = ('id', 'title', 'country', 'price', 'date_tour', 'image', 'description', 'done', 'created_at')
    read_only_fields = ('id', 'created_at')