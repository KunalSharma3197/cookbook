from django.db import models
from cookbook.mixins import AuthorTimeStampedModel
from django.contrib.auth.models import User

# Create your models here.

class Author(AuthorTimeStampedModel):
  user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author")
  bio = models.TextField(blank=True)
  profile_picture = models.ImageField(upload_to="profile_pictures/", blank=True)
  location = models.CharField(max_length=255, blank=True)
  website = models.URLField(blank=True)

  def __str__(self):
    return self.user.username
