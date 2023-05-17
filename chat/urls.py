from django.urls import path
from .views import index,roomf,stockdata


urlpatterns=[
    path('',index,name='home'),
    path("chat/<str:room_name>/", roomf, name="room"),
    path('data',stockdata,name='stock'),
]