from django.shortcuts import render
from modelform.forms import registerform
from modelform.models import register
# Create your views here.

def registerview(request):
    form = registerform()
    if request.method== "POST":
        form=registerform(request.POST)
        if form.is_valid():
            form.save()
            print("haii")
    return render(request,"base.html",{'form':form})



















'''
def registerview(request):
    form = registerform()
    if request.method== "POST":
        form=registerform(request.POST)
        if form.is_valid():
            user = form.cleaned_data['username']
            passw = form.cleaned_data['password']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            gender = form.cleaned_data['gender']
            age = form.cleaned_data['age']
            address = form.cleaned_data['address']
            print(user,passw,email,phone,gender,age,address)
            res= register.objects.create(username=user,password=passw,email=email,phone=phone,gender=gender,
            age=age,address=address)
            res.save()
            print("haii")
    return render(request,"base.html",{'form':form})
'''