from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def setting(request):
    return render(request, 'setting.html')

def profile(request):
    return render(request, 'profile.html')

def signin(request):
    return render(request, 'signin.html')

def signup(request):
    return render(request, 'signup.html')