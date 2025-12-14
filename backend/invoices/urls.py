from django.urls import path
from . import views

urlpatterns = [
    # We'll add API endpoints in Phase 3
    path('health/', views.health_check, name='health_check'),
]