from django.db import models
from django.contrib.contenttypes.models import ContentType

class Tag(models.Model):
    label = models.CharField(max_length=255)

class TagggedItem(models.Model):
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)