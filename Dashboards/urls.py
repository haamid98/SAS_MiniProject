from django.urls import path

from . import views

urlpatterns = [
    path('stuDash', views.stuDash, name='stuDash'),
    path('uniDash', views.uniDash, name='uniDash'),
    path('adminDash', views.adminDash, name='adminDash')
]