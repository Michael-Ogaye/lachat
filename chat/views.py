from django.shortcuts import render

# Create your views here.

def index(request):
   return render(request,'chat/index.html') 

def roomf(request, room_name):
    return render(request, "chat/room.html", {"room_name": room_name})
