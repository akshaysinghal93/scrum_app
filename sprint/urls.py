from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^add/$', 'sprint.views.addNewSprint', name='addNewSprint'),
	url(r'^view/$', 'sprint.views.viewAllSprints', name='viewAllSprints'),
	url(r'^edit/(?P<sprint_id>[0-9]+)$', 'sprint.views.updateSprint', name='updateSprint'),
)