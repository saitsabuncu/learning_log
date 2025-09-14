from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Topic, Entry

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "logs/index.html")


class TopicsView(View):
    def get(self, request):
        topics = Topic.objects.all()
        return render(request, "logs/topics.html", {"topics": topics})


class TopicDetailView(View):
    def get(self, request, topic_id):
        topic = get_object_or_404(Topic, id=topic_id)
        entries = topic.entry_set.order_by("-date_added")
        return render(request, "logs/topic_detail.html", {"topic": topic, "entries": entries})
