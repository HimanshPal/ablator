from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(r'^caniuse/(?P<client_user_string>[^/]+)/(?P<functionality_id>[^/]+)/?$', views.CanIUseView.as_view()),
    url(r'^which/(?P<client_user_string>[^/]+)/(?P<functionality_id>[^/]+)/?$', views.WhichView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)