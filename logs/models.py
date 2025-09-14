from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Topic(models.Model):
    """Kullanıcının öğrenmek istediği konular"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text
    
class Entry(models.Model):
    """Kullanıcının öğrendiği şeyler hakkında girdi"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="entries")
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return f"{self.text[:50]}..."    
