from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, AddCustomerForm
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

@login_required
def customer_record(request, pk):
    customer = Customer.objects.get(id=pk)
    return render(request, 'customer.html', {'customer': customer})

@login_required
def edit_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.first_name = request.POST['first_name']
        customer.last_name = request.POST['last_name']
        customer.phone_number = request.POST['phone_number']
        customer.email = request.POST['email']
        customer.address = request.POST['address']
        customer.city = request.POST['city']
        customer.state = request.POST['state']
        customer.zip_code = request.POST['zip_code']
        customer.save()
        messages.success(request, 'Customer record updated successfully.')
        return redirect('customer', pk=customer.id)
    else:
        return render(request, 'edit_customer.html', {'customer': customer})
    
@login_required
def add_customer(request):
    if request.method == 'POST':
        form = AddCustomerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New customer added successfully.')
            return redirect('home')
    else:
        form = AddCustomerForm()
    return render(request, 'add_customer.html', {'form': form})


@login_required
def delete_customer(request, pk):
    customer = Customer.objects.get(id=pk)
    if request.method == 'POST':
        customer.delete()
        messages.success(request, 'Customer record deleted successfully.')
        return redirect('home')
    else:
        return render(request, 'delete_customer.html', {'customer': customer})