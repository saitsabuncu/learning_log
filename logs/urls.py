from django.urls import path
from .views import IndexView, TopicsView, TopicDetailView

app_name = "logs"

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("topics/", TopicsView.as_view(), name="topics"),
    path("topics/<int:topic_id>/", TopicDetailView.as_view(), name="topic_detail"),
]
