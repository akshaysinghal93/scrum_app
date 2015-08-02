from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from scrum_teams.models import ScrumTeam
# Create your models here.

class UserProfileManager(BaseUserManager):
	def create_user(self, email, full_name, password=None):
		if not email:
			raise ValueError('User must have a valid email address')
		user=self.model(email=self.normalize_email(email),)
		user.full_name=full_name
		user.set_password(password)
		user.save(using=self._db)
		return user

	def create_superuser(self, email, full_name, password):
		user = self.create_user(email=email, full_name=full_name,
			password=password)
		user.is_admin = True
		user.is_superuser=True
		user.save(using=self._db)
		return user


class UserProfile(AbstractBaseUser , PermissionsMixin):
	"""
	Creates a User UserProfile
	"""
	email = models.EmailField('email address', unique=True, db_index=True, blank=False, null=False)
	full_name = models.CharField(default=False, blank=False, max_length=50,
		null=False)
	joined = models.DateTimeField(auto_now_add=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_superuser = models.BooleanField(default=False)
	scrum_team = models.ForeignKey(ScrumTeam, null=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['full_name']

	objects = UserProfileManager()

	def get_full_name(self):
		# The user is identified by their email address
		return self.email

	def get_short_name(self):
		# The user is identified by their email address
		return self.email

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		return True

	def has_module_perm(self, app_name):
		return True

	@property
	def is_staff(self):
		return self.is_admin

	def is_superuser(self):
		return self.is_admin