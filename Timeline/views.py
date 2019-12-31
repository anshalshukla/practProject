from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Feed
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User


def home(request):
    context = {"feeds": Feed.objects.all()}
    return render(request, "Timeline/timeline.html", context)


class PostListView(ListView):
    model = Feed
    template_name = "Timeline/timeline.html"
    context_object_name = "feeds"
    ordering = ["-date_posted"]
    paginate_by = 3


class UserPostListView(ListView):
    model = Feed
    template_name = "Timeline/user_feeds.html"
    context_object_name = "feeds"
    paginate_by = 3

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get("username"))
        return Feed.objects.filter(author=user).order_by("-date_posted")


class PostDetailView(DetailView):
    model = Feed


class PostCreateView(CreateView):
    model = Feed
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(UserPassesTestMixin, UpdateView):
    model = Feed
    fields = ["title", "content"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        feed = self.get_object()
        if self.request.user == feed.author:
            return True
        return False


class PostDeleteView(UserPassesTestMixin, DeleteView):
    model = Feed
    success_url = "/timeline"

    def test_func(self):
        feed = self.get_object()
        if self.request.user == feed.author:
            return True
        return False


def about(request):
    return render(request, "Timeline/about.html", {"title": "About"})
