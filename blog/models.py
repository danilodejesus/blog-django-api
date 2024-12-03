from django.db import models

# Create your models here.

class Category(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self): 
		  return self.name

class Post(models.Model):
  title = models.CharField(max_length=200)
  first_text = models.TextField(max_length=1000, null=True, blank=True)
  second_text = models.TextField(max_length=1000, null=True, blank=True)
  third_text = models.TextField(max_length=1000, null=True, blank=True)
  fourth_text = models.TextField(max_length=1000, null=True, blank=True)
  five_text = models.TextField(max_length=1000, null=True, blank=True)
  categories = models.ManyToManyField("Category", related_name="posts")
  created_at = models.DateTimeField(auto_now_add=True)
  country = models.CharField(max_length=50)
  main_image = models.ImageField(null=True, blank=True, upload_to="uploads/")
  
  def __str__(self): 
		  return self.title