from multiprocessing import context
from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Questions
# Create your views here.
def index(request):
    context= {
        'variable': 'this is sent........'
    }
    return render(request, "index.html", context)


def about(request):
    if request.method=="POST":
        question= request.POST.get("question")
        print(question)
        qa= Questions(question= question, date= datetime.today())
        qa.save()
    return render(request, "about.html")