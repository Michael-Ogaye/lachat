from django.shortcuts import render
from django.conf import settings

# Create your views here.

def index(request):
   return render(request,'chat/index.html') 

def roomf(request, room_name):
    mode=settings.MODE
    pro='ws' if mode=='dev'else 'wss'
    return render(request, "chat/room.html", {'prot':pro,'room_name':room_name})
