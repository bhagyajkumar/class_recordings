from django.http import HttpResponse
from django.shortcuts import render
from .models import Content, Subject


def home(request):
    subjects = Subject.objects.all()
    return render(request, "home.html", {"subjects": subjects})

def view_subject(request, id):
    subject = Subject.objects.get(id=int(id))
    contents = Content.objects.filter(subject=subject)
    return render(request, "view_subject.html", {"contents": contents, "subject": subject})
