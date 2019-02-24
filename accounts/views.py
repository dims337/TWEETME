from django.contrib.auth import get_user_model
from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView


User = get_user_model()

class UserDetailView(DetailView):
    queryset = User.objects.all()
    template_name="accounts/user_detail.html"
    #lookup_field = 'username'

    def get_object(self):
        return get_object_or_404(User, username__iexact=self.kwargs.get("username"))


