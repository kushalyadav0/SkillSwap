from django.urls import path
from .views import chat_api, recommendations_api, courses_api

urlpatterns = [
    path("chat/", chat_api),
    path("recommendations/", recommendations_api),
    path("courses/", courses_api),     
]
