from django.urls import path
from . import views

urlpatterns = [
    path('regUni', views.regUni, name='regUni')
]