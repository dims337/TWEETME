from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.forms.utils import ErrorList
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin


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



class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    success_url="/tweet/"
    template_name = "tweets/update_view.html"




class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('home')

