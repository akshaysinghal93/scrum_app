from django.shortcuts import render
from django.shortcuts import render_to_response, redirect, render
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from .forms import AddSprintForm
from .models import Sprint
# Create your views here.
@login_required(login_url='/app/login/')
def addNewSprint(request):
	"""
	Add Sprint
	"""
	if(request.method == 'POST'):
		form = AddSprintForm(data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('/app/sprint/view')
	else:
			form = AddSprintForm()
	return render_to_response('addUpdateSprint.html', {
		'form' : form,
	}, context_instance=RequestContext(request))

@login_required(login_url='/app/login/')
def updateSprint(request, sprint_id=None):
	"""
	Update existing sprint
	"""
	if(request.method == 'POST'):
		form = AddSprintForm(request.POST)
		if form.is_valid():
			sprint = Sprint(
			sprint_id = form.cleaned_data.get('sprint_id'),
			sprint_name = form.cleaned_data.get('sprint_name'),
			sprint_from_date = form.cleaned_data.get('sprint_from_date'),
			sprint_to_date = form.cleaned_data.get('sprint_to_date'))
			sprint.save()
		return redirect('/app/sprint/view')
	else:
		sprint = Sprint.objects.get(sprint_id=sprint_id)
		form = AddSprintForm(instance=sprint)
		return render_to_response('addUpdateSprint.html', {
			'form' : form,
		}, context_instance=RequestContext(request))

@login_required(login_url='/app/login/')
def viewAllSprints(request):
	"""
	View All Sprints
	"""
	sprints = Sprint.objects.all()
	return render_to_response('viewSprints.html', {
		'sprints' : sprints,
	}, context_instance=RequestContext(request))