from django.urls import path
from .views import index,roomf


urlpatterns=[
    path('',index,name='home'),
    path("chat/<str:room_name>/", roomf, name="room"),
]