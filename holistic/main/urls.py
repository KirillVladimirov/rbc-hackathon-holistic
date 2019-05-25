from django.urls import path
from .views import index
app_name = "main"

# Backend office URLs
urlpatterns = [
    path("", index, name="index"),

]
