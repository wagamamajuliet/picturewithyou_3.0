from rest_framework import serializers
from . import models
from taggit_serializer.serializers import (TagListSerializerField,
											TaggitSerializer)
from picturewithyou.users import models as user_models

class SmallImageSerializer(serializers.ModelSerializer):
	""" Used for the notifications """
	class Meta:
		model = models.Image
		fields = (
			'file'
		)

class CountImageSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Image
		fields = (
			'id',
			'file',
			'comment_count',
			'like_count'
		)

class FeedUserSerializer(serializers.ModelSerializer):
	class Meta:
		model = user_models.User
		fields = (
			'username',
			'profile_image'
		)

class CommentSerializer(serializers.ModelSerializer):

	creator = FeedUserSerializer(read_only=True)

	class Meta:
		model = models.Comment
		fields = (
			'id',
			'message',
			'creator'
		)

class LikeSerializer(serializers.ModelSerializer):

	class Meta:
		model = models.Like
		fields = '__all__'


class InputImageSerializer(serializers.ModelSerializer):

	file = serializers.FileField(required=False)

	class Meta:
		model = models.Image
		fields = (
			'file',
			'location',
			'caption',
		)

class ImageSerializer(TaggitSerializer,serializers.ModelSerializer):

	comments = CommentSerializer(many=True)
	# likes = LikeSerializer(many=True)
	creator = FeedUserSerializer()
	tags = TagListSerializerField()

	class Meta:
		model = models.Image
		fields = (
			'id',
			'file',
			'location',
			'caption',
			# 'comment_set',
			# 'like_set',
			'comments',
			'like_count',
			'creator',
			'tags',
			'natural_time'
		)	
