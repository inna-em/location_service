from django.urls import path
from .views import LocationView

urlpatterns = [
    path('info/', LocationView.as_view())
]