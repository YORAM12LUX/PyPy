from django.shortcuts import  redirect, render
from django.http import HttpResponseRedirect  
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login

from authentification.apps import AuthentificationConfig

#import authentification 

# Create your views here.

def home(request):
    return render(request,"authentification/index.html")


def signup(request):
    if request == "POST":
        #username=request.POST.get('username')
        username = request.POST.get('username')
        nom = request.POST.get('nom')
        pnom = request.POST.get('pnom')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        myuser= User.objects.create_user(username,email,pass1)
        myuser.nom= nom
        myuser.pnom=pnom

        myuser.save()

        messages.success(request,"Votre compte a été créer avec succès")

        return redirect('signin')


    return render(request,"authentification/signup.html")

def signin(request):

    if request == "POST":
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        user = AuthentificationConfig(username=username, password=pass1)

        if user is not None:
            login(request,user)
            nom =user.nom
            return render(request,"authetification/index.html",{'nom':nom})
        else:
            messages.error(request,"Mauvais")
            return HttpResponseRedirect('home')
        
    return render(request,"authentification/signin.html")

def signout(request):
    pass