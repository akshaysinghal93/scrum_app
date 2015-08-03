from django import forms
from .models import Sprint
# from scrum_teams.models import ScrumTeam

class AddSprintForm(forms.ModelForm):
	"""
	Form to add new sprint
	"""
	sprint_id = forms.CharField(widget=forms.HiddenInput(), initial=-1)
	sprint_name = forms.CharField(widget=forms.TextInput, label='Sprint Name')
	sprint_from_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}),
		label='From Date')
	sprint_to_date = forms.DateField(widget=forms.TextInput(attrs={'class': 'datepicker'}),
		label='To Date')
	# scrum_team = forms.ModelChoiceField(queryset=ScrumTeam.get_scrum_teams(),
	#  empty_label="--Select Team--", widget=forms.Select(attrs={'class':'combobox'}))

	class Meta:
		model = Sprint
		fields = ['sprint_name', 'sprint_id', 'sprint_from_date', 'sprint_to_date']
		# fields = ['sprint_name', 'sprint_from_date', 'sprint_to_date', 'scrum_team']

	def clean(self):
		cleaned_data = super(AddSprintForm, self).clean()
		return self.cleaned_data

	def save(self, commit=True):
		team = super(AddSprintForm, self).save(commit=False)
		if commit:
			# print 'Data save: %s' % self.cleaned_data
			team.save()
		return team