from django.shortcuts import render
from portfolio.models import Portfolio
from pricing.models import Basic, Standard, Premium

from .models import Team, Service

# Create your views here.

def index(request):
    portfolio = Portfolio.objects.all()
    team = Team.objects.all()
    service = Service.objects.all()
    basic = Basic.objects.all()
    standard= Standard.objects.all()
    premium= Premium.objects.all()
    context = {
        'portfolio': portfolio,
        'team' : team,
        'basic' : basic,
        'standard': standard,
        'premium': premium,
        'service':service
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
