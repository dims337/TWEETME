from django.conf.urls import url

from .views import TweetDetailView,TweetListView, TweetCreateView


urlpatterns = [
   # url(r'^admin/', admin.site.urls),
    url(r'^$', TweetListView.as_view(), name='list'),
    url(r'^(?P<pk>\d+)/$', TweetDetailView.as_view(), name='detail'),#tweet/1
    url(r'^create/$', TweetCreateView.as_view(), name='create'),#/tweet/create
]