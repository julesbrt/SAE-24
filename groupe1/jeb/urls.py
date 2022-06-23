from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path("capteur/info.html",views.capteur),
    path('capteur/update/<int:id>', views.update),
    path('capteur/info/<int:id>', views.updatetraitement),
    path("donnee/info.html", views.donnee),
    path('capteur/info/<int:id>', views.export_csv),
]
