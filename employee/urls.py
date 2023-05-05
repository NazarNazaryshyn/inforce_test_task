from django.urls import path
from .views import GetEmployeeAPIView, RegisterAPIView, VoteForMenuAPIView


urlpatterns = [
    path("", GetEmployeeAPIView.as_view()),
    path("create/", RegisterAPIView.as_view()),
    path("vote_for/", VoteForMenuAPIView.as_view())
]
