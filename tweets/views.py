from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"



class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context
    template_name = 'tweets/list_view.html'    



class TweetCreateView(FormUserNeededMixin,CreateView):
    #queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url="/tweet/create/"
    login_url = "/admin/" #redirect to login page when user not authenticated



