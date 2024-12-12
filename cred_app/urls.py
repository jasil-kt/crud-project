from django.urls import path

from cred_app import views

urlpatterns = [
    path('',views.landing,name="landing"),
    path('index',views.index,name="index")
]