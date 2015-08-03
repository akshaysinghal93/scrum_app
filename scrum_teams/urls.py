from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^edit/remove_user/(?P<email>[\w.@+-]+)/$', 
		'scrum_teams.views.removeTeamMembers', name='removeTeamMembers'),
	url(r'^add/$', 'scrum_teams.views.addNewScrumTeam', name='addNewScrumTeam'),
	url(r'^edit/(?P<team_id>[0-9]+)/$', 
		'scrum_teams.views.updateScrumTeam', name='updateScrumTeam'),
	url(r'^edit/userTeam/(?P<team_id>[0-9]+)/$', 
		'scrum_teams.views.addTeamMembers', name='addTeamMembers'),
	url(r'^$', 'scrum_teams.views.viewAllTeams', name='viewAllTeams'),
	# url(r'^view$', 'scrum_teams.views.viewStories', name='viewStories'),
)