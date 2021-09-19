from django.shortcuts import render ,get_object_or_404
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.

from .models import Subject
from django.contrib.auth.models import User

def index (request):
    return render(request,"subjects/index.html",{
        "subjects": Subject.objects.all(),
        "user":request.user,
})

def subject (request,subject_id):
    subject = get_object_or_404(Subject,pk=subject_id)
    my =Subject.objects.filter(pk=subject_id)

    return render(request,"subjects/subject.html",{
        "subject": subject,"course": my,"user":request.user,
    })

def Course (request):
    my =request.user.studentlist.all()
    return render(request,"subjects/MyCourse.html",{

        "course": my,

    })



def enroll (request,subject_id):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    subject = get_object_or_404(Subject,pk=subject_id)


    me  = Subject.objects.filter(pk=subject_id)

    for x in me:
        print(request.user in x.studentInClass.all())

    if subject.limited_seat < 1:
            Subject.objects.filter(pk=subject_id).update(status="full")
    elif  request.user not in x.studentInClass.all():
            subject.studentInClass.add(request.user)
            Subject.objects.filter(pk=subject_id).update(seat=(subject.seat-1))


    return HttpResponseRedirect(reverse("subjects:subject",args=(subject_id,)))



def drop (request,subject_id):
    subject = get_object_or_404(Subject,pk=subject_id)
    me  = Subject.objects.filter(pk=subject_id)

    for x in me:
        print(request.user in x.studentInClass.all())


    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if  subject.studentInClass.count()+subject.seat == subject.limited_seat:
        Subject.objects.filter(pk=subject_id).update(status="free")

    if request.user in x.studentInClass.all():
        print(request.user in x.studentInClass.all())
        subject.studentInClass.remove(request.user)
        Subject.objects.filter(pk=subject_id).update(seat=(subject.seat+1))



    return HttpResponseRedirect(reverse("subjects:subject",args=(subject_id,)))



