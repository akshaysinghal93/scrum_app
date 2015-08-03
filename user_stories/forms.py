from django import forms
from .models import UserStory
from sprint.models import Sprint

class UpdateUserStoryForm(forms.ModelForm):
	"""
	Form for creating/updating a user story.
	"""
	story_id = forms.CharField(widget=forms.HiddenInput(), initial=-1)
	story_ref = forms.CharField(widget=forms.TextInput, label='Story Reference')
	story_title = forms.CharField(widget=forms.TextInput, label='Story Title')
	story_desc = forms.CharField(widget=forms.Textarea, label='Story Description')
	effort_required = forms.IntegerField(widget=forms.TextInput, label='Required Effort')
	sprint = forms.ModelChoiceField(queryset=Sprint.objects.all(), 
		empty_label='---Select Sprint----',
		widget=forms.Select(attrs={'class':'combobox'}))
	
	class Meta:
		model = UserStory
		fields = ['story_id', 'story_ref', 'story_title', 'story_desc', 'effort_required', 'sprint']

	def clean(self):
		cleaned_data = super(UpdateUserStoryForm, self).clean()
		return self.cleaned_data

	def save(self, commit=True):
		story = super(UpdateUserStoryForm, self).save(commit=False)
		if commit:
			story.save()
		return story
