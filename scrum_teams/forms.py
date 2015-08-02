from django import forms
from .models import ScrumTeam

class UpdateScrumTeamForm(forms.ModelForm):
	"""
	Form for creating/updating a scrum team
	"""
	team_id = forms.CharField(widget=forms.HiddenInput(), initial=-1)
	team_name = forms.CharField(widget=forms.TextInput, label='Scrum Team Name')

	class Meta:
		model = ScrumTeam
		fields = ['team_id', 'team_name']

	def clean(self):
		cleaned_data = super(UpdateScrumTeamForm, self).clean()
		return self.cleaned_data

	def save(self, commit=True):
		team = super(UpdateScrumTeamForm, self).save(commit=False)
		if commit:
			print 'Data save: %s' % self.cleaned_data
			team.save()
		return team

class UpdateTeamMembers(forms.ModelForm):
	"""
	Form to add/remove members to scrum team
	"""
	team_name = forms.CharField(widget=forms.TextInput)
		