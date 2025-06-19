from django.urls import path
from .views import ChatView, GenerateAPIKeyView

urlpatterns = [
    path("chat/", ChatView.as_view()),
    path('generate-key/', GenerateAPIKeyView.as_view()),
]