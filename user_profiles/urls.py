from django.conf.urls import patterns, url

urlpatterns = patterns('',
	url(r'^dashboard$', 'user_profiles.views.dashboard', name='dashboard'),
	url(r'^register$', 'user_profiles.views.register', name='register'),
	url(r'^login$', 'user_profiles.views.login', name='login'),
	url(r'^logout$', 'user_profiles.views.logout', name='logout'),
)