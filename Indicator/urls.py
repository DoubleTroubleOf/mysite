from django.urls import path

from . import views

app_name= 'indicators'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('add_indicators', views.add_indicators, name='add_indicators')
]