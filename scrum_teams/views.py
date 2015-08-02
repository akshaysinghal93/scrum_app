from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from .forms import UpdateScrumTeamForm

# Create your views here.
def updateScrumTeam(request):
	"""
	Add/Update User Scrum Team
	"""
	if(request.method == 'POST'):
		form = UpdateScrumTeamForm(data=request.POST)
		if form.is_valid():
			if request.user.is_admin:
				new_team = form.save()
				return render(request, "dashboard.html", {'template_title' : request.user.email})
			else:
				return redirect('/app/login')
	else:
		try:
			data = {
			'team_id' : request.team_id,
			'team_name' : request.team_name
			}
			form = UpdateScrumTeamForm(data)
		except AttributeError:
			form = UpdateScrumTeamForm()
	return render_to_response('addUpdateScrumTeam.html', {
		'form' : form,
	}, context_instance=RequestContext(request))