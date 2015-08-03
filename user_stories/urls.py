from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^add/$', 'user_stories.views.addUserStory', name='addUserStory'),
	url(r'^edit/(?P<story_id>[0-9]+)$', 'user_stories.views.updateUserStory', name='updateUserStory'),
	url(r'^board/$', 'user_stories.views.getScrumBoard', name='getScrumBoard'),
	url(r'^view/$', 'user_stories.views.viewAllStories', name='viewAllStories'),
	# url(r'^view$', 'scrum_teams.views.viewStories', name='viewStories'),
)