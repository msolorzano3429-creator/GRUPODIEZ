from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'Core/home.html')
def corto(request):
    return render(request, 'Core/corto.html')