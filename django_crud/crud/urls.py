from venv import create
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("user/", views.UserListView.as_view()),
    path("create/", views.create, name='create')
]