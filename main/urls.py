from django.urls import path
from . import views

urlpatterns = [
    path('submit_application/', views.submit_application),
    path('subscribe/', views.subscribe)
]