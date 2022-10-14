from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path("medicine/", views.medicine),
    path("medicine/add", views.medicine_add, name="medicine_add"),
    path("illness/", views.illnes_list, name="illness_list"),
    path("illness/add", views.illness_add, name="illness_add"),
    path("illness/<int:pk>", views.illness_info, name="illness_info"),
    path("illness/edit/<int:pk>", views.illness_edit, name="illness_edit"),
    path("illness/delete/<int:pk>", views.illness_delete, name="illness_delete"),
    
    path("times/", views.times_list, name="times_list"),
    path("time/add/", views.time_add, name="time_add"),
    
    path("notification/", views.notification, name="notification_list"),
    path("notification/add/", views.notification_add, name="notification_add"),
    path("notification/<int:pk>/", views.notification_info, name="notification_info"),
    path("notification/edit/<int:pk>/", views.notification_edit, name="notification_edit"),
    path("notification/delete/<int:pk>/", views.notification_delete, name="notification_delete"),

    
]
