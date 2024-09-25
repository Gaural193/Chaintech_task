from django.urls import path
from .views import * 

urlpatterns = [
    path('index', index,name="index"),
    path('form',form,name="form"),
    path('data',data,name="data")
]