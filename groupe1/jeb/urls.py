from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("capteur/info.html",views.capteur),
    path("update/<int:id>/", views.update),
    path("updatetraitement/<int:id>/", views.updatetraitement),
    path("donnee/info.html", views.donnee)
]
