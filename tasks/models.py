from django.db import models

# Create your models here.
class Task(models.Model):
  title = models.CharField(max_length=100)
  country = models.CharField(max_length=100, null=True, blank=True)
  price = models.CharField(max_length=10, null=True, blank=True)
  date_tour = models.CharField(max_length=50, null=True, blank=True)
  image = models.ImageField(upload_to='uploads/', null=True, blank=True)
  description = models.TextField(null=True, blank=True)
  done = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)