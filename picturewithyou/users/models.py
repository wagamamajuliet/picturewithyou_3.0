from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _

@python_2_unicode_compatible
class User(AbstractUser):

	GENDER_CHOICES = (
		('male', 'Male'),
		('female', 'Female'),
		('not-specified', 'Not specified')
	)
    # First Name and Last Name do not cover name patterns
    # around the globe.
	profile_image = models.ImageField(null=True)
	name = models.CharField(_("Name of User"), blank=True, max_length=255)
	website = models.URLField(null=True)
	bio = models.TextField(null=True)
	phone = models.CharField(max_length=140, null=True)
	gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)
	following = models.ManyToManyField("self", blank=True)
	followers = models.ManyToManyField("self", blank=True)
	# //blank=True가 아니면 굵은 폰트로 변경되고 이 뜻은 필수필드라는 뜻이 된다
	def __str__(self):
		return self.username

	@property
	def post_count(self):
		return self.images.all().count()

	@property
	def followers_count(self):
		return self.followers.all().count()

	@property
	def following_count(self):
		return self.following.all().count()