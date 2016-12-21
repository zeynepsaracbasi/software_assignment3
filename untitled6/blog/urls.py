from django.conf.urls import url

from .views import show_blog, get_blog

urlpatterns = [
    url('entries/$', show_blog),
    url('entries/(?P<blog_id>[0-9]+)', get_blog)
]

