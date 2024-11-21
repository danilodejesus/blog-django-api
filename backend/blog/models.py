from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=30)

class Post(models.Model):
  title = models.CharField(max_length=200)
  created_at = models.DateTimeField(auto_now_add=True)
  country = models.CharField(max_length=50)
  main_image = models.ImageField(null=True, blank=True, upload_to="uploads/")
  main_description = models.TextField(null=True, blank=True)
  h1_title = models.CharField(max_length=70)
  h1_image = models.ImageField(null=True, blank=True, upload_to="uploads/")
  h2_title = models.CharField(max_length=70)
  h2_description = models.CharField(max_length=200)
  h2_image = models.ImageField(null=True, blank=True, upload_to="uploads/")
  h3_title = models.CharField(max_length=70)
  h3_description = models.CharField(max_length=200)
  h3_image = models.ImageField(null=True, blank=True, upload_to="uploads/")
  categories = models.ManyToManyField("Category", related_name="posts")
