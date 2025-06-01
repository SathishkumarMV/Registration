from django.urls import path, include
from .views import *

urlpatterns = [
 path("", home, name="home"),
 path("signup/", AuthView, name="AuthView"),
 path("accounts/", include("django.contrib.auth.urls")),
]