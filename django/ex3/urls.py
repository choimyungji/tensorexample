from django.conf.urls import patterns, url

from . import views

urlpatterns = patterns('',
	url(r'^articles/2003/$', views.special_case_2003),
	url(r'^articles/(\d{4})/$', views.year_archive),
	url(r'^articles/(\d{4})/(\d{2})/$', views.month_archive),
	url(r'^articles/(\d{4})/(\d{2})/(\d+)/$', views.article_detail),
)
