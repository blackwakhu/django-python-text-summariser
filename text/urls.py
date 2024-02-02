from django.urls import path
from . import views


urlpatterns =[
  path("", views.index, name="index"),
  path("summarise/", views.summariser, name="summariser"),
  path("summarise/text/", views.summarise_text, name="summarise_text"),
  path("summarise/url/", views.summarise_url, name="summarise_url"),
]
