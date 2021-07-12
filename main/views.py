from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
# Create your views here.

def login(request):
    if request.method == 'POST':
        userName = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=userName,password=password)
        if user:
            auth.login(request,user)
            # value = User.objects.get(username=userName)
            # print(value)
            if user.is_superuser:
                return redirect('app_admin')
            return redirect('/',username=userName)
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    return render(request,'login.html')

def register(request):

    if request.method == 'POST':
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        userName = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password']
        password2 = request.POST['password2']
        if password1 == password2:
            if not User.objects.filter(username=userName).exists():
                if not User.objects.filter(email=email).exists():
                    user = User.objects.create_user(username=userName,password=password1,email=email,first_name=firstName,last_name=lastName)
                    user.save()
                    messages.info(request,'account created successfully')
                    return redirect('register')
                else:
                    messages.info(request,'email is already taken')
                    return redirect('register')
            else:
                print(userName)
                messages.info(request,'username is already taken')
                return redirect('register')
        else:
            messages.info(request,'password is not matching')
            return redirect('register')
    return render(request,'register.html')

def app_admin(request):
    return render(request,'admin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def home(request):
    return render(request,"home.html")

