from django.db import models
from rest_framework import serializers

# Create your models here.
class Post(models.Model):
    post = models.TextField()

class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
