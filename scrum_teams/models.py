from django.db import models

# Create your models here.
class ScrumTeam(models.Model):
	team_id = models.AutoField(primary_key=True, db_index=True, blank=True)
	team_name = models.CharField(max_length=50, blank=False, default='Default')

	def __unicode__(self):
		return self.team_name