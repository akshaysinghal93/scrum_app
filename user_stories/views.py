from django.shortcuts import render_to_response, redirect, render
from django.template import RequestContext
from .forms import UpdateUserStoryForm

# Create your views here.
def updateUserStory(request):
	"""
	Add/Update User Story View
	"""
	if(request.method == 'POST'):
		form = UpdateUserStoryForm(data=request.POST)
		if form.is_valid():
			if request.user.is_admin:
				new_story = form.save()
				return render(request, "dashboard.html", {'template_title' : request.user.email})
			else:
				return redirect('/app/login')
	else:
		try:
			data = {
				'story_id': request.story_id,
				'story_ref' : request.story_ref,
				'story_title' : request.story_title,
				'story_desc' : request.story_desc,
				'effort_required' : request.effort_required
			}
			form = UpdateUserStoryForm(data)
		except AttributeError:
			form = UpdateUserStoryForm()

	return render_to_response('addUpdateUserStory.html', {
		'form' : form,
	}, context_instance=RequestContext(request))
