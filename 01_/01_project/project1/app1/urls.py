
from django.urls import path
from . import views

urlpatterns = [
   
    path('',views.app1_all,name = "app1_all"),
]