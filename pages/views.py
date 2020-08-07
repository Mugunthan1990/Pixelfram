from django.shortcuts import render
from portfolio.models import Portfolio

# Create your views here.

def index(request):
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio': portfolio
    }
    return render(request, 'pages/index.html',context)

def about(request):
    return render(request, 'pages/about.html')
