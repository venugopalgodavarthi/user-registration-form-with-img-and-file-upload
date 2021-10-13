from django.shortcuts import render
from upload.forms import formregister,loginform
from upload.models import register
# Create your views here.

def viewregister(request):
    form = formregister()
    if request.method=="POST" and request.FILES:
        form = formregister(request.POST,request.FILES)
        if form.is_valid():
            form.save()

    return render(request,"formregister.html",{"form":form})


def loginview(request):
    form = loginform()
    if request.method=="POST":
        form = loginform(request.POST)
        if form.is_valid():
            print("login")
   
    return render(request,"login.html",{'form':form})

def details(request):
    res= register.objects.all()
    return render(request,"details.html",{'res':res})
