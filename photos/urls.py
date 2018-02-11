from django.urls import path
from . import views

app_name = 'photos'
urlpatterns = [
    path('<int:photo_id>/', views.detail, name='detail'),
]