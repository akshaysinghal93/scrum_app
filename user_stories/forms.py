from django import forms
from .models import UserStory

class UpdateUserStoryForm(forms.ModelForm):
	"""
	Form for creating/updating a user story.
	"""
	story_id = forms.CharField(widget=forms.HiddenInput(), initial=-1)
	story_ref = forms.CharField(widget=forms.TextInput, label='Story Reference')
	story_title = forms.CharField(widget=forms.TextInput, label='Story Title')
	story_desc = forms.CharField(widget=forms.Textarea, label='Story Description')
	effort_required = forms.IntegerField(widget=forms.TextInput, label='Required Effort')
	
	class Meta:
		model = UserStory
		fields = ['story_id', 'story_ref', 'story_title', 'story_desc', 'effort_required']

	def clean(self):
		cleaned_data = super(UpdateUserStoryForm, self).clean()
		return self.cleaned_data

	def save(self, commit=True):
		story = super(UpdateUserStoryForm, self).save(commit=False)
		if commit:
			print 'Data save: %s' % self.cleaned_data
			story.save()
		return story
