from django.db import models
from user_stories.models import UserStory
from user_profiles.models import UserProfile
# Create your models here.
class Task(models.Model):
	task_id = models.AutoField(primary_key=True, db_index=True, blank=True)
	task_name = models.CharField(max_length=50, blank=False)
	task_description = models.CharField(max_length=250, blank=False)
	task_status = models.CharField(max_length=20, blank=False, default='To-Do')
	user = models.ForeignKey(UserProfile, null=True, unique=False, blank=True)
	effort_required = models.IntegerField(null=False, blank=False, default=10)
	story = models.ForeignKey(UserStory, null=True, unique=False, blank=True)

	def __str__(self):
		return self.task_name
