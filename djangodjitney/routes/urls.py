from django.urls import path
from .views import LinesView, CreateLineView, UpdateLineView, DeleteLineView

from . import views

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path("lines/", views.LinesView.as_view(), name="lines"),
  path('lines/new/', CreateLineView.as_view(), name='create_line'),  
  path('lines/<pk>/update/', views.UpdateLineView.as_view(), name='update_line'),
  path('lines/<int:pk>/delete/', views.DeleteLineView.as_view(), name='delete_line'),
  path("stations/", views.StationsView.as_view(), name="stations"),
  path('station/new/', views.CreateStationsView.as_view(), name='create_station'), 
  path('station/<pk>/update/', views.UpdateStationsView.as_view(), name='update_station'),
  path('station/<int:pk>/delete/', views.DeleteStationsView.as_view(), name='delete_station'),
  path("stops/", views.StopView.as_view(), name="stops"),
  path('stops/new/', views.CreateStopView.as_view(), name='create_stop'), 
  path('stops/<pk>/update/', views.UpdateStopView.as_view(), name='update_stop'),
  path('stops/<int:pk>/delete/', views.DeleteStopView.as_view(), name='delete_stop'),
]
