from django.conf.urls import patterns, include, url
from views import draw, h, hello

urlpatterns = patterns('',('^$', hello),('^([^/]+)$', draw),('^hai/$', h),
   
)
