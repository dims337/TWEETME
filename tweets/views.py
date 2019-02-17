from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from .models import Tweet
from .forms import TweetModelForm

# Create your views here.
# def tweet_detail_view(request, id=1):
#     obj = Tweet.objects.get(id=id)
#     context = {
#         'object': obj,
#     }
#     return render (request, 'tweets/detail_view.html', context)


#  def tweet_list_view(request):
#     queryset = Tweet.objects.all()
#     context = {
#         "object_list": queryset,
#     }
#     return render (request, 'tweets/list_view.html', context) 


class TweetDetailView(DetailView):
    queryset = Tweet.objects.all()
    template_name = "tweets/detail_view.html"



class TweetListView(ListView):
    queryset = Tweet.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(TweetListView, self).get_context_data(*args, **kwargs)
        return context
    template_name = 'tweets/list_view.html'    



class TweetCreateView(CreateView):
    #queryset = Tweet.objects.all()
    form_class = TweetModelForm
    template_name = "tweets/create_view.html"
    success_url="/tweet/create/"

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TweetCreateView, self).form_valid(form)


