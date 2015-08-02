from django.db import models

# Create your models here.
class ScrumTeam(models.Model):
	team_id = models.AutoField(primary_key=True, db_index=True, blank=True)
	team_name = models.CharField(max_length=50, blank=False, default='Default')

	def __unicode__(self):
		return self.team_name

	@classmethod
	def get_scrum_teams(self, scrum_team_name=None):
		if not scrum_team_name:
			return ScrumTeam.objects.all().order_by('team_name')
		else:
			return ScrumTeam.objects.filter(team_name=scrum_team_name)

	@classmethod
	def get_scrum_team_by_id(self, scrum_team_id=None):
		return ScrumTeam.objects.get(team_id__exact=scrum_team_id)

