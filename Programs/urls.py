from django.urls import path
from . import views

urlpatterns = [
    path('addProg', views.addProg, name='addProg')
]
