from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import DetailView
from django.views import View

from .models import UserProfile


User = get_user_model()

class UserDetailView(DetailView):
    
    template_name="accounts/user_detail.html"
    queryset = User.objects.all()
    #lookup_field = 'username'

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))



class UserFollowView(View):
    def get(self,request,username, *args, **kwargs):
        toggle_user = get_object_or_404( User, username__iexact=username)
        if request.user.is_authenticated:
            is_following = UserProfile.objects.toggle_follow(request.user, toggle_user)
        
        return redirect ("profiles:detail", username=username)
