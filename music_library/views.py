from django.http import JsonResponse
from django.shortcuts import render

from music_library.models import *

# Create your views here.
def return_albums(request):
    cd = Album.objects.all().values()
    data = list(cd)
    return JsonResponse({'albums': data})

def return_songs(request):
    #set what you want to get to a variable
    song = Song.objects.all().values()
    #make it into a list
    data = list(song)
    #return as json data with a key:value pair
    return JsonResponse({'songs': data})
