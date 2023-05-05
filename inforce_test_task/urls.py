from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("restaurant/", include("restaurant.urls")),
    path("employee/", include("employee.urls")),
    path("auth/", include("authentication.urls")),
]
