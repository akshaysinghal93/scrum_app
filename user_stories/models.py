from django.db import models

# Create your models here.
class UserStory(models.Model):
	story_id = models.AutoField(primary_key=True, db_index=True, blank=True)
	story_ref = models.CharField(max_length=10, blank=False, unique=True)
	story_title = models.CharField(max_length=200, blank=False)
	story_desc = models.CharField(max_length=1000, blank=False)
	effort_required = models.IntegerField()
	

	def __unicode__(self):
		return "%s : %s ..." % (self.story_ref, self.story_desc[0:100],)