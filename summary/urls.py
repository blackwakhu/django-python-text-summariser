from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("get summary/", views.get_summary, name="get summary"),
    path("display/<str:word>", views.display_results, name="display summary")
]
