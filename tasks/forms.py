from django import forms
from .models import Task
from user_stories.models import UserStory

class CreateTaskForm(forms.ModelForm):
	"""
	Form for creating new tasks
	"""
	CHOICES = (
		('To-Do', 'To-Do'),
		('In-Progress', 'In-Progress'),
		('Completed', 'Completed'),
	)
	task_id = forms.CharField(widget=forms.HiddenInput(), initial=-1)
	task_name = forms.CharField(widget=forms.TextInput, label='Task Name')
	task_description = forms.CharField(widget=forms.TextInput, label='Task Description')
	task_status = forms.ChoiceField(choices=CHOICES, required=True, label='Status'
		, widget=forms.Select(attrs={'class':'combobox'}))
	effort_required = forms.CharField(widget=forms.TextInput, 
		label='Effort Required', initial=10, required=False)
	
	class Meta:
		model = Task
		fields = ['task_id', 'task_name', 'task_description', 'task_status', 'effort_required']
		exclude = ['user', 'story']

	def clean(self):
		cleaned_data = super(CreateTaskForm, self).clean()
		return self.cleaned_data

	def save(self, commit=True):
		story = super(CreateTaskForm, self).save(commit=False)
		if commit:
			# print 'Data save: %s' % self.cleaned_data
			story.save()
		return story