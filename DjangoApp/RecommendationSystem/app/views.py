from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def index(req):
#     return HttpResponse("<h1>Hello World</h1>")

database = {
    "action" : ["baahubali","kgf","hulk","batman","superman","thor","avengers",
                "spiderman","aquaman","antman","baahubali 2"],
    "comedy" : ["zero","dhamaal","hera pheri","stree","welcome","golmaal"],
    "horror" : ["annabelle","conjuring","the ring","stree"],
    "biopic" : ["ms dhoni","sanju","mary kom"],
    "thriller" : ["annabelle","conjuring","sixth sense","seven"]
    }

def index(req):
    return render(req,"index.html",context={"data":database})