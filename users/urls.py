from django.urls import path

from .views import get_current_user

app_name = "users"
urlpatterns = [
    path("me/", view=get_current_user, name="get-current-user"),
]
