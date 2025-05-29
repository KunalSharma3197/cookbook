from django.db import models
from cookbook.mixins import AuthorTimeStampedModel, IsDeletedMixin

# Create your models here.

class File(AuthorTimeStampedModel, IsDeletedMixin):
  file = models.FileField(upload_to="files/")
  name = models.CharField(max_length=255)
  description = models.TextField(blank=True)
  file_type = models.CharField(max_length=255)
  s3_key = models.CharField(max_length=255)

  def __str__(self):
    return self.name