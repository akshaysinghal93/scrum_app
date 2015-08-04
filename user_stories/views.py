from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from .forms import UpdateUserStoryForm
from .models import UserStory
from tasks.models import Task
from sprint.models import Sprint
# Create your views here.


@login_required(login_url='/app/login/')
def addUserStory(request):
	"""
	Add User Story View
	"""
	if(request.method == 'POST'):
		form = UpdateUserStoryForm(data=request.POST)
		print "form %s " % form
		if form.is_valid():
			new_story = form.save()
			return redirect('/app/stories/view')
		else:
			print "Operation failed"
			raise ValidationError('Form had some errors')
	else:
		form = UpdateUserStoryForm()
		return render_to_response('addUpdateUserStory.html', {
			'form' : form,
		}, context_instance=RequestContext(request))

@login_required(login_url='/app/login/')
def updateUserStory(request, story_id=None):
	"""
	Update existing user story
	"""
	if(request.method == 'POST'):
		form = UpdateUserStoryForm(request.POST)
		if form.is_valid():
			userStory = UserStory(
			story_id = form.cleaned_data.get('story_id'),
			story_ref = form.cleaned_data.get('story_ref'),
			story_title = form.cleaned_data.get('story_title'),
			story_desc = form.cleaned_data.get('story_desc'),
			effort_required = form.cleaned_data.get('effort_required'),
			sprint = form.cleaned_data.get('sprint'))
			userStory.save()
		return redirect('/app/stories/view')
	else:
		print "Loadin get data"
		story = UserStory.objects.get(story_id=story_id)
		data = {
			'story_id': story.story_id,
			'story_ref' : story.story_ref,
			'story_title' : story.story_title,
			'story_desc' : story.story_desc,
			'effort_required' : story.effort_required,
			'sprint' : story.sprint
		}
		form = UpdateUserStoryForm(instance=story)
		return render_to_response('addUpdateUserStory.html', {
			'form' : form,
		}, context_instance=RequestContext(request))


@login_required(login_url='/app/login/')
def viewAllStories(request):
	"""
	View All User Stories
	"""
	userStories = UserStory.objects.all()
	return render_to_response('viewStories.html', {
		'userStories' : userStories,
	}, context_instance=RequestContext(request))

@login_required(login_url='/app/login/')
def getScrumBoard(request):
	"""
	View All User Stories
	"""
	if (request.method == 'GET'):
		try:
			sprint_id = request.GET.get('sprint_id')
			sprint=Sprint.objects.get(sprint_id=sprint_id)
			selected_sprint = sprint.sprint_name
		except:
			sprint = None
			selected_sprint = ""
	userStories = UserStory.objects.filter(sprint=sprint)
	print "userStories %s" % userStories
	tasks_to_do = Task.objects.filter(task_status='To-Do')
	tasks_in_progress = Task.objects.filter(task_status='In-Progress')
	tasks_completed = Task.objects.filter(task_status='Completed')
	return render_to_response('scrumBoard.html', {
		'userStories' : userStories,
		'tasks_to_do' : tasks_to_do,
		'tasks_in_progress' : tasks_in_progress,
		'selected_sprint' : selected_sprint,
		'tasks_completed' : tasks_completed,
		'sprints' : Sprint.objects.all()
	}, context_instance=RequestContext(request))
