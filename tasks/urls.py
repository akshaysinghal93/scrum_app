from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^add/(?P<story_id>[0-9]+)/$', 
		'tasks.views.createNewTask', name='createNewTask'),
	url(r'^assign/(?P<task_id>[0-9]+)/$', 
		'tasks.views.assignTaskToUser', name='assignTaskToUser'),
	url(r'^unassign/(?P<task_id>[0-9]+)/$', 
		'tasks.views.unassignTaskUser', name='unassignTaskUser'),
	url(r'^change_status/$',
	 'tasks.views.changeStatus', name='changeStatus'),
)