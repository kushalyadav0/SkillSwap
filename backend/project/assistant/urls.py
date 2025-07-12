from django.urls import path
from . import views

urlpatterns = [
    path("chat/", views.chat_api, name="chat_api"),
    path("recommendations/", views.recommendations_api, name="recs_api"),
]
