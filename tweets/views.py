from django.contrib.auth.mixins import LoginRequiredMixin
from django import forms
from django.db.models import Q
from django.forms.utils import ErrorList
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from .models import Tweet
from .forms import TweetModelForm
from .mixins import FormUserNeededMixin, UserOwnerMixin


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/tweet_detail.html"



class TweetListView(ListView):
    #queryset = Tweet.objects.all()

    def get_queryset(self, *args, **kwargs):
        qs = Tweet.objects.all().order_by("-timestamp")
        query = self.request.GET.get("q", None)
        if query is not None:
            qs = qs.filter(
                Q(content__icontains=query) |
                Q(user__username__icontains=query))
        return qs


    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        context['create_form'] = TweetModelForm()
        context['create_url'] = reverse_lazy("tweet:create")
        return context
    template_name = 'tweets/tweet_list.html'    



class TweetCreateView(FormUserNeededMixin,CreateView):
    #queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    #success_url = reverse_lazy('tweet:detail')
    login_url = "/admin/" #redirect to login page when user not authenticated



class TweetUpdateView(LoginRequiredMixin, UserOwnerMixin, UpdateView):
    queryset = Tweet.objects.all()
    form_class = TweetModelForm
    #success_url="/tweet/"
    template_name = "tweets/update_view.html"




class TweetDeleteView(LoginRequiredMixin, DeleteView):
    model = Tweet
    template_name = 'tweets/delete_confirm.html'
    success_url = reverse_lazy('tweet:list')

