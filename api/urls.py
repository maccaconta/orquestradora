from .views import (ApiOrchest, index, ApiLoginSP, ApiLoginSPRedirect,
                    ApiLoginSPCrentials, monitorAttendance, removeAttendance)
from django.urls import path

urlpatterns = [
    path('watson/', ApiOrchest.as_view()),
    path('monitor/',monitorAttendance,  name='monitorAttendance'),
    path('remove/', removeAttendance, name='removeAttendance'),
    path('loginsp/', ApiLoginSP, name='ApiLoginSP'),
    path('openid/', ApiLoginSPCrentials, name='ApiLoginSPCrentials'),
    path('login/', ApiLoginSPRedirect, name="ApiLoginSPRedirect"),
    path('index/', index, name='index')
]


