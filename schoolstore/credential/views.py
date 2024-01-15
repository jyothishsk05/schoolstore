from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect



def login(request):
    if request.method == 'POST':
        username = request.POST['username'],
        password = request.POST['password'],
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, User)
            return render('index.html')
        else:
            messages.info(request, "invalid credentials")
            return redirect('login')
    return render(request, "login.html")

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['confirm_password']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken")
                return redirect("register")

            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password mismatch")
            return redirect('register')

    return render(request, 'register.html')
def Details(request):

    return render(request, 'details.html')

