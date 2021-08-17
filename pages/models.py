from django.db import models
from django_resized import ResizedImageField
# Create your models here.
class Team(models.Model):
    # portfolio = models.Foreignkey(Portfolio, on_delete=models.DO_NOTHING)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    # moduleimage = ResizedImageField(quality=100,default='-')
    img = models.ImageField(upload_to="img",null=True,blank=True)

    is_published =models.BooleanField(default=True)
    def __str__(self):
        return self.name


class Service(models.Model):
    # portfolio = models.Foreignkey(Portfolio, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=200, blank=True)
    icon = models.ImageField(upload_to="img",null=True,blank=True)

    is_published =models.BooleanField(default=True)
    def __str__(self):
        return self.title
