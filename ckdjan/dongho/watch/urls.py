from django.urls import path
from . import views

urlpatterns = [
    path('', views.watch_list, name='watch_list'),
    path('watch/<int:pk>/', views.watch_detail, name='watch_detail'),

]