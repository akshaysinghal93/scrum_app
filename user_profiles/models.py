from django.db import models
from django.contrib.auth.models import AbstractBaseUser
# Create your models here.




class UserProfile(AbstractBaseUser):
	"""
	Creates a User UserProfile
	"""
	email = models.EmailField('email address', unique=True, db_index=True, blank=False, null=False)
	full_name = models.CharField(default=False, blank=False, max_length=50,
		null=False)
	joined = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['full_name']

	def __unicode__(self):
		return self.email