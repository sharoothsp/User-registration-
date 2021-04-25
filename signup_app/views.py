from django.shortcuts import render, redirect
from .forms import regForm, loginForm
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.
def home(request):
    if request.method == 'POST':
        logform = regForm(request.POST or None)
        if logform.is_valid():
            name = logform.cleaned_data["First_name"]
            email = logform.cleaned_data["Email"]
            pass1 = logform.cleaned_data["Password"]
            pass2 = logform.cleaned_data["Repassword"]
            term = logform.cleaned_data["terms"]
        if pass1 == pass2 and term == True:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
            elif User.objects.filter(username=name).exists():
                messages.info(request,'Username already exist')
            else:
                user = User.objects.create_user(username=name, password=pass1, email=email)
                user.save()
                return redirect('login')
        else:
            messages.info(request,'Incorrect password')

    else:
        logform = regForm()


    context = {
        'form' : logform

    }
    return render(request, 'signup\signup.html', context)


def login(request):
    if request.method == 'POST':
        loginform = loginForm(request.POST)
        if loginform.is_valid():
            name = loginform.cleaned_data['Username']
            password = loginform.cleaned_data['Password']
            user = auth.authenticate(username=name,password=password)
            if user is not None:
                auth.login(request, user)
                #print("login Confirm")
                return redirect('/login')
            else:
                messages.info(request,'invalid username or password')
                #print("failed")
    else:
        loginform = loginForm()

    context = {
    'loginform':loginform


    }
    return render(request,'signup\login.html', context)


def logout(request):
    auth.logout(request)
    return redirect('/')
