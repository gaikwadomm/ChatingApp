from django.shortcuts import render,redirect
from .models import Room, Message
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'home.html')

#2.AFTER ENTRING THE ROOM NAME PRESENT IN THE DATA BASE THE ROOM INFORMATION WILL DISPLAY WITH THE HELP OF THIS
def room(request, room):
    if not request.user.is_authenticated:
        messages.info(request, "Please log in to access the chat room.")
        return redirect('home')
    
    username = request.user.username #GET THE USERNAME FROM WHO IS LOGGED IN
    room_details = Room.objects.get(name = room)

    return render(request, 'room.html',{
        'username': username,
        'room': room,
        'room_details': room_details,
    })

#1.AT FIRST THE HOME PAGE WILL WORK BY THIS 
def checkview(request):
    if request.method == 'POST':
        room = request.POST['room_name']
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            if Room.objects.filter(name = room).exists():
                return redirect('/'+room)
            #else:
                #new_room = Room.objects.create(name=room)
                #new_room.save()
                #return render(request, 'home.html')'''

            else:
                messages.info(request, "THE ROOM IS NOT PRESENT.")
                return render(request, 'home.html')
        else:
            messages.info(request, "Invalid username or password.")
            return render(request, 'home.html')
    else:
        return render(request, 'home.html')

#3.THIS WILL SAVE THE MESSAGES SEND AFTER OPENING THE ROOM 
def send(request):
    if request.method == 'POST':
        message = request.POST['message']
        username = request.user.username
        room_id = request.POST['room_id']

        new_message = Message.objects.create(value=message, user=username, room=room_id)
        new_message.save()

        return HttpResponse('Message send successfully.')
    else:
        return render(request, 'room.html')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages": list(messages.values())})