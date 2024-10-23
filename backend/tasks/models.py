from django.db import models

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=100)
  country = models.CharField(max_length=100)
  price = models.CharField(max_length=10)
  date_tour = models.CharField(max_length=50)
  image = models.ImageField(upload_to='uploads/')
  description = models.TextField(null=True, blank=True)
  done = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)