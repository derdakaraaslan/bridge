from django.urls import path, include
from .api_v1 import api

urlpatterns = [
    path("", api.urls),
]
