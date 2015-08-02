from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from .forms import UpdateScrumTeamForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from .models import ScrumTeam
from user_profiles.models import UserProfile

# Create your views here.

def addNewScrumTeam(request):
	"""
	Add Scrum Team
	"""
	if(request.method == 'POST'):
		form = UpdateScrumTeamForm(data=request.POST)
		if form.is_valid():
			if request.user.is_admin:
				new_team = ScrumTeam(team_name=form.cleaned_data.get('team_name'))
				new_team.save()
				return redirect('/app/teams/')
			else:
				return redirect('/app/login')
	else:
			form = UpdateScrumTeamForm()
	return render_to_response('addUpdateScrumTeam.html', {
		'form' : form,
	}, context_instance=RequestContext(request))


def updateScrumTeam(request, team_id=None):
	"""
	Update User Scrum Team
	"""
	if(request.method == 'POST'):
		form = UpdateScrumTeamForm(data=request.POST)
		if form.is_valid():
			if request.user.is_admin:
				new_team = ScrumTeam(team_id=form.cleaned_data.get('team_id'),
					team_name=form.cleaned_data.get('team_name'))
				new_team.save()
				return redirect('/app/teams/')
			else:
				return redirect('/app/login')
	else:
		try:
			data = {
			'team_id' : team_id,
			'team_name' : ScrumTeam.objects.get(pk=team_id)
			}
			non_members = UserProfile.get_users_by_team()
			members = UserProfile.get_users_by_team(team_id)
			form = UpdateScrumTeamForm(data)
		except AttributeError:
			form = UpdateScrumTeamForm()
	return render_to_response('addUpdateScrumTeam.html', {
		'form' : form,
		'members' : members,
		'non_members' : non_members,
	}, context_instance=RequestContext(request))

def viewAllTeams(request):
	"""
	View All Scrum Teams
	"""
	scrum_teams = ScrumTeam.get_scrum_teams()
	return render_to_response('viewTeams.html', {
		'scrum_teams' : scrum_teams,
	}, context_instance=RequestContext(request))

def addTeamMembers(request, team_id=-1):
	"""
	Edit Users Scrum Team
	"""
	if(request.method == 'POST'):
		try:
			print "Selected user: %s" % request.POST['selectedUser']
			user= UserProfile.change_user_team(email=request.POST['selectedUser']
				, scrum_team=ScrumTeam.get_scrum_team_by_id(scrum_team_id=team_id))
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		except:
		 	print "Operation Failed"
		 	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def removeTeamMembers(request, email=None):
	"""
	Edit Users Scrum Team
	"""
	if(request.method == 'GET'):
		try:
			print "Selected Email: %s" % email
			user= UserProfile.change_user_team(email=email
				, scrum_team=None)
			return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
		except:
		 	print "Operation Failed"
		 	return HttpResponseRedirect(request.META.get('HTTP_REFERER'))