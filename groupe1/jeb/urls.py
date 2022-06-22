from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('donnee/info.html', views.home),

]