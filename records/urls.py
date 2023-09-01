from django.urls import path
from .views import createLog,showLogs
urlpatterns = [
    path('create',createLog,name="create-log"),
    path('',showLogs,name="show-logs")
]