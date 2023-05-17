from django.shortcuts import render
from django.conf import settings

# Create your views here.
mode=settings.MODE
pro='ws' if mode=='dev'else 'wss'

def index(request):
   return render(request,'chat/index.html') 

def roomf(request, room_name):
    
    return render(request, "chat/room.html", {'prot':pro,'room_name':room_name})
def stockdata(request):
    return render(request,'chat/chart.html',{'prot':pro})
    