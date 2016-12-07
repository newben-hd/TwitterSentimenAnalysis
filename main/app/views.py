from django.shortcuts import render
from source.mining import *
import json

# Create your views here.
def index(request):
    tweets = []
    if "q" in request.GET:
        tweets = getTweetObject(request.GET["q"])
    context = {
        "tweets": tweets,
    }
    return render(request, "index.html", context)
