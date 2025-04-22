from rest_framework import serializers
from .models import Post
from users.models import User

class PostSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='author.name')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'author', 'author_name', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at', 'author_name']