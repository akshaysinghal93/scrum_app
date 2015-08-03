from django.db import models
# from scrum_teams.models import ScrumTeam
# Create your models here.
class Sprint(models.Model):
	sprint_id = models.AutoField(primary_key=True, db_index=True, blank=True)
	sprint_name = models.CharField(max_length=30, blank=False, unique=True)
	sprint_from_date = models.DateField(auto_now=False, auto_now_add=False, blank=False)
	sprint_to_date = models.DateField(auto_now=False, auto_now_add=False ,blank=False)
	# scrum_team = models.OneToOneField(ScrumTeam)

	def __str__(self):
		return self.sprint_name

	@classmethod
	def get_sprint_by_name(self, sprint_name=None):
		if not sprint_name:
			return Sprint.objects.order_by('sprint_name').all()
		else:
			return Sprint.objects.order_by('sprint_name').filter(sprint_name=sprint_name)