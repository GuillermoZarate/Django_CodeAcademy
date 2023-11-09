from django.urls import path
from .views import LinesView, CreateLineView, UpdateLineView, DeleteLineView

from . import views

urlpatterns = [
  path('', views.HomeView.as_view(), name='home'),
  path("lines/", views.LinesView.as_view(), name="lines"),
  path('lines/new/', CreateLineView.as_view(), name='create_line'),  
  path('lines/<pk>/update/', UpdateLineView.as_view(), name='update_line'),
  path('lines/<int:pk>/delete/', DeleteLineView.as_view(), name='delete_line')
]
