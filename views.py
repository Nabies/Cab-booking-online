from django.shortcuts import render
from django.core.mail import send_mail,BadHeaderError
from .models import Booking,Driver
from .forms import BookingForm,Driverform,UserForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
# Create your views here.
def index(request):
    form=BookingForm()
    registered=False
    if request.method=='POST':
        form=BookingForm(data=request.POST)
        if form.is_valid():
            user_detail=form.save()
            print(user_detail)
            registered=True
            return redirect('index')


    return render(request,'index.html',context={'myform':form})

def contact(request):
    if request.method=="POST":
        proj_name=request.POST['name']
        proj_email=request.POST['email']
        proj_subject=request.POST['subject']
        proj_message=request.POST['message']

        send_mail(
            proj_name,
            proj_message,
            proj_email,
            ['jonathanjhonnyamarwal@gmail.com'],
            fail_silently=False,
        )

        return render(request,'contact.html',{'name':proj_name})
    else:
        return render(request,'contact.html',{})


def driver(request):
    p=Driverform()
    user_form = UserForm()
    registered=False
    if request.method=="POST":
        user_form = UserForm(data=request.POST)
        p=Driverform(data=request.POST)
        print(p.is_valid(),end=" ")
        print("hello")
        print(user_form.is_valid())
        if user_form.is_valid() and p.is_valid() :
            # driver_details=p.save()
            # print(driver_details)

            x=user_form.save()
            x.set_password(x.password)
            x.save()
            p.save(x.username)
            registered=True
            user=user_form.cleaned_data.get('username')
            messages.success(request,'The Account was created for '+ user)
            return redirect('login')


    # print(p)
    return render(request,'driver.html',context={'detailsform':p,'userform':user_form})
@login_required
def bookingdetails(request):
    # bookingdetails=Booking.objects.filter()
    bookingdetails=Booking.objects.all()
    return render(request,'detail.html',context={'bookingdetails':bookingdetails})

@login_required
def driverdetails(request):
    driverdetails=Driver.objects.all()
    print(driverdetails)
    print(request)
    return render(request,'driverdetails.html',context={'driverdetails':driverdetails})


def loginform(request):
    if request.method =='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(request,username=username,password=password)

        if user is not None:
            login(request,user)
            return redirect('details')
        else:
            messages.info(request,'The Username or Password is Incorrect')

    return render(request,'login.html',context={})

def logoutform(request):
    logout(request)
    return redirect('login')
