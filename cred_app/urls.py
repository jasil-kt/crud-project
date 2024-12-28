from django.urls import path

from cred_app import views

urlpatterns = [
    path('',views.landing,name="landing"),
    path('index',views.index,name="index"),
    path('read',views.read,name="read"),
    path("delete_data/<int:id>/",views.delete_data,name="delete_data"),
    path("update_data/<int:id>/",views.update_data,name="update_data")
]