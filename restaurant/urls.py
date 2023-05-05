from django.urls import path
from .views import ResturantAPIView, MenuAPIView, GetCurrentDayMenusAPIView

urlpatterns = [
    path("", ResturantAPIView.as_view()),
    path("menu/", MenuAPIView.as_view()),
    path("get_current_day_menus/", GetCurrentDayMenusAPIView.as_view())
]
