from rest_framework import serializers
from .models import Post, Comment, Tag
from users.models import User

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['name']

class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    date = serializers.ReadOnlyField(source='created_at')
    tags = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'description', 'author', 'date', 'tags', 'imageUrl']
        read_only_fields = ['id', 'date', 'author']

    def get_tags(self, obj):
        return [tag.name for tag in obj.tags.all()]

    def create(self, validated_data):
        tags_data = self.context.get('request').data.get('tags', [])
        post = Post.objects.create(**validated_data)

        # Handle tags
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            post.tags.add(tag)

        return post

    def update(self, instance, validated_data):
        tags_data = self.context.get('request').data.get('tags', [])

        # Update Post fields
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.imageUrl = validated_data.get('imageUrl', instance.imageUrl)
        instance.save()

        # Handle tags
        instance.tags.clear()
        for tag_name in tags_data:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            instance.tags.add(tag)

        return instance

class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.name')
    date = serializers.ReadOnlyField(source='created_at')

    class Meta:
        model = Comment
        fields = ['id', 'postId', 'author', 'date', 'content', 'likes']
        read_only_fields = ['id', 'date', 'author']
