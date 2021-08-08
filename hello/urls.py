from django.urls import path

from .views import hello

app_name = "hello"
urlpatterns = [
    path("", view=hello, name="hello-world"),
    path("<path:resource>", view=hello, name="hello-path"),
]
