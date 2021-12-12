
from django.shortcuts import render,HttpResponse
from datetime import datetime
from .models import Contact, Himani
from .models import Triund
from django.contrib import messages
from .models import Kareri
from .models import Thatharana
from .models import Indrahara
from .models import Rising



# Create your views here.
#def index(request):
    #return HttpResponse("homepage")
    
def index(request):
    #context={"variable":'this is sent'}
    

    

    #messages.success(request,'This is a text message!')
    #return HttpRespons("Homepage")
    return render(request,'index.html')
def about(request):
    #return HttpResponse("about")
    return render(request,'about.html')
def contact(request):
    #return HttpResponse("contact")

    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        contact=Contact(name=name,email=email,phone=phone,date=datetime.today())
        messages.success(request, 'messsage has been sent.')


        
        contact.save()
    return render(request,'contact.html')
    

def services(request):
    #return HttpResponse("services")
    return render(request,'services.html')
def triund(request):

    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get('email')
        person=request.POST.get('person')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        phone=request.POST.get('number')
        date=request.POST.get('date')
        triund=Triund(name=name,email=email,person=person,zip=zip,state=state,phone=phone,date=date)
        messages.success(request,'submitted')
        triund.save()
        


    return render(request,'triund.html')

def kareri(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get('email')
        person=request.POST.get('person')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        phone=request.POST.get('number')
        date=request.POST.get('date')
        kareri=Kareri(name=name,email=email,person=person,zip=zip,state=state,phone=phone,date=date)
        messages.success(request,'submitted')
        kareri.save()
        
    return render(request,'kareri.html')


def thatharana(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get('email')
        person=request.POST.get('person')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        phone=request.POST.get('number')
        date=request.POST.get('date')
        thartharana=Thatharana(name=name,email=email,person=person,zip=zip,state=state,phone=phone,date=date)
        messages.success(request,'submitted')
        thartharana.save()
        



    return render(request,'thatharana.html')


def himani(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get('email')
        person=request.POST.get('person')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        phone=request.POST.get('number')
        date=request.POST.get('date')
        himani=Himani(name=name,email=email,person=person,zip=zip,state=state,phone=phone,date=date)
        messages.success(request,'submitted')
        himani.save()
    return render(request,'himani.html')

def indra(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get('email')
        person=request.POST.get('person')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        phone=request.POST.get('number')
        date=request.POST.get('date')
        himani=Himani(name=name,email=email,person=person,zip=zip,state=state,phone=phone,date=date)
        messages.success(request,'submitted')
        himani.save()
    return render(request,'indra.html')



def rising(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get('email')
        person=request.POST.get('person')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        phone=request.POST.get('number')
        date=request.POST.get('date')
        rising=Rising(name=name,email=email,person=person,zip=zip,state=state,phone=phone,date=date)
        messages.success(request,'submitted')
        rising.save()
    return render(request,'rising.html')



def laka(request):
    if request.method=='POST':
        name=request.POST.get("name")
        email=request.POST.get('email')
        person=request.POST.get('person')
        state=request.POST.get('state')
        zip=request.POST.get('zip')
        phone=request.POST.get('number')
        date=request.POST.get('date')
        laka=Rising(name=name,email=email,person=person,zip=zip,state=state,phone=phone,date=date)
        messages.success(request,'submitted')
        laka.save()
    return render(request,'laka.html')






        

    
    