from django.shortcuts import render,redirect
from .models import Turufs
from . forms import bookingform

# Create your views here.
def index(request):
    return render(request,'index.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
def booking(request):
    if request.method=="POST":
        form=bookingform(request.POST)
        if form.is_valid():
            form.save()
            print("success")
            return redirect('/')
    form=bookingform()
    dictbook={
        'form':form
    }
    return render(request,'booking.html',dictbook)
def turufs(request):
    dict_tr={
        'turf':Turufs.objects.all()
    }
    return render(request,'turufs.html',dict_tr)





