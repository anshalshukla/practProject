from django.urls import path
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    UserPostListView,
)
from . import views


urlpatterns = [
    path("", PostListView.as_view(), name="timeline-home"),
    path("user/<str:username>", UserPostListView.as_view(), name="user-feeds"),
    path("feed/<int:pk>/", PostDetailView.as_view(), name="feed-detail"),
    path("feed/<int:pk>/update/", PostUpdateView.as_view(), name="feed-update"),
    path("feed/<int:pk>/delete/", PostDeleteView.as_view(), name="feed-delete"),
    path("feed/new/", PostCreateView.as_view(), name="feed-create"),
    path("about/", views.about, name="timeline-about"),
]

# <apps>/<model>_<viewtype>.html

