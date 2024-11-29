from django.shortcuts import render, redirect
from .forms import ServiceRequestForm
from .models import ServiceRequest
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout 

def register_view(request):
    if request.method == 'POST':
        form =UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username' :'', 'password1':'', 'password2':''}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'register.html',{'form':form})

def login_view(request):
    if request.method == 'POST':
        form =AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request,user)
            return redirect('dashboard')
    else:
        initial_data = {'username' :'', 'password1':''}
        form = AuthenticationForm(initial=initial_data)
    return render(request, 'login.html',{'form':form})

def dashboard_view(request):
    return render (request, 'dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def submit_service_request(request):
    if request.method == 'POST':
        form = ServiceRequestForm(request.POST, request.FILES)
        if form.is_valid():
            service_request = form.save(commit=False)
            service_request.customer = request.user  
            service_request.save()
            return redirect('service_request_detail', pk=service_request.pk)
    else:
        form = ServiceRequestForm()

    return render(request, 'submit_request.html', {'form': form})

@login_required
def service_request_detail(request, pk):
    service_request = ServiceRequest.objects.get(pk=pk)
    return render(request, 'service_request_detail.html', {'service_request': service_request})

@login_required
def track_service_requests(request):
    service_requests = ServiceRequest.objects.filter(customer=request.user)
    return render(request, 'track_requests.html', {'service_requests': service_requests})

from django.contrib.auth.decorators import user_passes_test
def is_support_rep(user):
    return user.groups.filter(name='Support').exists()

@user_passes_test(is_support_rep)
def manage_requests(request):
    open_requests = ServiceRequest.objects.filter(status='Pending')
    return render(request, 'manage_requests.html', {'open_requests': open_requests})
