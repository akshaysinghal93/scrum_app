from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from .forms import CreateTaskForm
from .models import Task
from user_stories.forms import UserStory
from django.contrib.auth.decorators import login_required
import json

# Create your views here.

@login_required(login_url='/app/login/')
def createNewTask(request, story_id=None):
	"""
	Function to create new task
	"""
	if(request.method == 'POST'):
		form = CreateTaskForm(data=request.POST)
		if form.is_valid():
			task_name = form.cleaned_data.get('task_name')
			task_description = form.cleaned_data.get('task_description')
			task_status = form.cleaned_data.get('task_status')
			story = UserStory.objects.get(story_id=story_id)
			task = Task(task_name=task_name, task_description=task_description,
				task_status=task_status, story=story)
			task.save()
			return redirect('/app/stories/view')
		else:
			print "Operation Failed"
			return redirect('/app/stories/view')
	else:
		form = CreateTaskForm()
		return render_to_response('createNewTask.html', {
			'form' : form,
		}, context_instance=RequestContext(request))

@login_required(login_url='/app/login/')
def assignTaskToUser(request, task_id=None):
	"""
	Assign task to user
	"""
	if(request.method == 'GET'):
		task = Task.objects.get(task_id=task_id)
		if task.user != None and task.user != request.user:
			return HttpResponseForbidden()
		task.user = request.user
		task.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/app/login/')
def unassignTaskUser(request, task_id=None):
	"""
	Unassign task to user
	"""
	if(request.method == 'GET'):
		task = Task.objects.get(task_id=task_id)
		if task.user != None and task.user != request.user:
			return HttpResponseForbidden()
		task.user = None
		task.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required(login_url='/app/login/')
def changeStatus(request):
	"""
	Change task status
	"""
	if(request.method == 'POST'):
		task = Task.objects.get(task_id=request.POST.get('task_id'))
		print "Task Name %s" % task.task_name
		print "Task Status before %s" % task.task_status
		if task.user == None or task.user != request.user:
		 	return HttpResponse(json.dumps('failure')
		 		,content_type="application/json")
		task.task_status = request.POST.get('status')
		print "Task %s " % task.task_status
		try:
			task.save()
		except:
			print "Operation failed"
		return HttpResponse(json.dumps('success'),content_type="application/json")
