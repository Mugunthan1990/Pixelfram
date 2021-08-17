from django.shortcuts import render

from .models import Basic, Standard, Premium

# Create your views here.


def index(request):
   basic= Basic.objects.all()
   standard= Standard.objects.all()
   premium= Premium.objects.all()
   context= {'basic': basic,'standard': standard,'premium': premium }
   return render(request, 'pages/index.html', context)
