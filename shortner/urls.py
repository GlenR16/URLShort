from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('about',views.about,name='about'),
    path('links',views.links,name='links'),
    path('create',views.create,name='create'),
    path('delete',views.delete,name='delete'),
    path('<str:pk>',views.go,name='go'),
]