from rest_framework import serializers

from posts.models import Comment, Group, Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    post = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id',
                  'author',
                  'post',
                  'text',
                  'created')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id',
                  'title',
                  'slug',
                  'description')


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    group = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id',
                  'text',
                  'pub_date',
                  'author',
                  'image',
                  'group')
