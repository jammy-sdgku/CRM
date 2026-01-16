from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegisterForm
from .models import Customer


def home(request):
    customers = Customer.objects.all()
    
    if request.method == 'POST':
        username = request.POST['userName']
        password = request.POST['password']
        #authenticate
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Your login is successful!')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password.')
            return redirect('home')
    else:   
        return render(request, 'home.html', {'customers': customers}) 


def logout_user(request):
    logout(request)
    messages.info(request, 'You have been logged out...')
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #Authenticate and login user
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            messages.success(request, 'Registration successful.')
            return redirect('home')
        else:
            messages.error(request, 'Unsuccessful registration. Invalid information.')
            return redirect('register')
    else:
        form = RegisterForm()
        return render(request, 'register.html', {'form': form})
    
def customer_record(request, pk):
    if request.user.is_authenticated:
        customer = Customer.objects.get(id=pk)
        return render(request, 'customer.html', {'customer': customer})
    else:
        messages.error(request, 'You must be logged in to view this page.')
        return redirect('home')