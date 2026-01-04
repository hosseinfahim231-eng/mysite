
from django.urls import path
from website.views import http_test

urlpatterns = [
    path('http-test', http_test),
]