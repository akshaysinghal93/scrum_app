from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^add$', 'user_stories.views.updateUserStory', name='updateUserStory'),
	# url(r'^view$', 'scrum_teams.views.viewStories', name='viewStories'),
)