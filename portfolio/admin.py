from django.contrib import admin
from .models import Portfolio



# Register your models here.

from embed_video.admin import AdminVideoMixin
from .models import Portfolio

class MyModelAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Portfolio, MyModelAdmin)
