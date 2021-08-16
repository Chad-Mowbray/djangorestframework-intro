from rest_framework import serializers
from .models import BlogPost
from django.contrib.auth.models import User


class BlogPostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = BlogPost
        fields = ['author', 'title', 'body']