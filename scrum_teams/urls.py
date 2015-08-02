from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^add$', 'scrum_teams.views.updateScrumTeam', name='updateScrumTeam'),
	# url(r'^view$', 'scrum_teams.views.viewStories', name='viewStories'),
)