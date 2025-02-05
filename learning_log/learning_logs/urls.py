""" learnin_logs için URL örüntülerini tanımlar."""
from django.urls import path, include
from . import views

app_name='learning_logs'
urlpatterns = [
    #Ana sayfa.
    path('', views.index, name='index'),
    #Bütün konuları gösteren sayfa.
    path('topics/', views.topics, name='topics'),
    path('Topics/', views.topics, name='topics_capital'),  # Büyük harfli yönlendirme
    #tek bir konu için ayrıntı sayfası.
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    #Yeni Konu eklemek için olan sayfa
    path('new_topic/', views.new_topic, name='new_topic'),  # Bu satırı ekle
    #Yeni bir girdi eklemek için olan sayfa.
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),
    #bir girdiyi düzenlemek için olan sayfa.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    path('users/', include('users.urls')),  # Users uygulamasının URL'leri
    
]