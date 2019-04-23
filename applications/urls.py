from django.urls import path
from . import views

urlpatterns = [
    path('apply', views.applyUni, name='apply'),
    path('deleteApply', views.delApplication, name='deleteApply'),
    path('updateProg', views.updateProgress, name='updateProg')
]