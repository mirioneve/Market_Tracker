from django.shortcuts import render
# Create your views here.
def index(request):
    return render(request, "marketapp/index.html")

def dashboard(request):
    return render(request, "marketapp/dashboard.html")

def products(request):
    return render(request, "marketapp/products.html")

