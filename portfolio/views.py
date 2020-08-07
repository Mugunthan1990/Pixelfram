from django.shortcuts import render

from .models import Portfolio

# Create your views here.


def index(request):
   allItems= Portfolio.objects.all()
   context= {'allitems': allItems}
   return render(request, 'pages/index.html', context)
