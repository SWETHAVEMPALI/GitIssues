from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', github, name='github'),
]