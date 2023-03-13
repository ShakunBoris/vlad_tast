from django.urls import path
from . import views

app_name = 'vlad'
urlpatterns = [
    path('', views.index, name='index'),
    path('save', views.save, name='save'),
    path('show', views.show, name='show'),
]
