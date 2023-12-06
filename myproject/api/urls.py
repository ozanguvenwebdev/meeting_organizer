from django.urls import path
from . import views

urlpatterns = [
    path('meetings/', views.getMeetings, name="meetings"),
    path('meetings/create/', views.createMeeting, name="create-meeting"),
    path('meetings/<str:pk>/update/', views.updateMeeting, name="update-meeting"),
    path('meetings/<str:pk>/delete/', views.deleteMeeting, name="delete-meeting"),

]
