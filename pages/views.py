from django.shortcuts import render
from portfolio.models import Portfolio
from .models import Team

# Create your views here.

def index(request):
    portfolio = Portfolio.objects.all()
    team = Team.objects.all()
    context = {
        'portfolio': portfolio,
        'team' : team
    }
    return render(request, 'pages/index.html',context)

def about(request):
    team = Team.objects.all()
    context = {
        'team' : team
    }
    return render(request, 'pages/about.html' ,context)

def contact(request):
    return render(request, 'pages/contact_us.html')


def portfolio(request):
    portfolio = Portfolio.objects.all()
    context = {
        'portfolio': portfolio
    }
    return render(request, 'pages/portfolio.html',context)
