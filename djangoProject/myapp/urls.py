from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('about/',views.about),
    path('hello/<str:userName>',views.hello),
    path('projects/',views.projects),
    path('task/<str:descriptionn>',views.task)
]