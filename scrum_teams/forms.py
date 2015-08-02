from django import forms
from .models import ScrumTeam
from user_profiles.models import UserProfile

class UpdateScrumTeamForm(forms.Form):
	"""
	Form for creating/updating a scrum team
	"""
	team_id = forms.CharField(widget=forms.HiddenInput(), initial=-1)
	team_name = forms.CharField(widget=forms.TextInput, label='Scrum Team Name')
	# non_members = forms.ModelMultipleChoiceField(queryset=UserProfile.get_users_by_team())
	# members = forms.ModelMultipleChoiceField(queryset=UserProfile.get_users_by_team())

	class Meta:
		model = ScrumTeam
		fields = ['team_id', 'team_name' 'non_members', 'members']

	def clean(self):
		cleaned_data = super(UpdateScrumTeamForm, self).clean()
		return self.cleaned_data

	def save(self, commit=True):
		team = super(UpdateScrumTeamForm, self).save(commit=False)
		if commit:
			print 'Data save: %s' % self.cleaned_data
			team.save()
		return team

# class ViewScrumTeams(forms.ModelForm):
# 	"""
# 	Form to add/remove members to scrum team
# 	"""
	
