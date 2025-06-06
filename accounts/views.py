from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def register(request):

    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lname')
        mail = request.POST.get('mail')
        password = request.POST.get('pass')
        cpass = request.POST.get('cpass')
        username = request.POST.get('username')

        if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()or(password != cpass): 
            messages.info(request, 'Username or Email already exists or Passwords do not match')
            return render(request, 'register.html')
        else:
             User.objects.create_user(username=username, first_name=fname, email=mail,last_name=lname,password=password)
             User.save()
             print("User Created") #will print our server terminal
             return redirect('/')
    else:
       return render(request, 'register.html')