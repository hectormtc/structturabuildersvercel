# apps/accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, CustomerForm
from .models import Customer


def logout_view(request):
    logout(request)
    return redirect('login')

def customer_profile(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST, instance=request.user.customer)
        if form.is_valid():
            form.save()
            return redirect('service_search')
    else:
        form = CustomerForm(instance=request.user.customer)
    return render(request, 'accounts/profile.html', {'form': form})


def dashboard(request):
    return render(request, 'dashboard.html')