
from django.urls import path,include
from . import views
from .views import *

urlpatterns = [
   
    path('review', views.review, name="review"),
]