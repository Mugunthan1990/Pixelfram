from django.db import models
# from embed_video.fields import EmbedVideoField


# Create your models here.


class Basic(models.Model):
    # portfolio = models.Foreignkey(Portfolio, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    deliverabels1 =  models.CharField(max_length=200,null=True)
    deliverabels2 =  models.CharField(max_length=200,null=True)
    deliverabels3 =  models.CharField(max_length=200,null=True)
    deliverabels4 =  models.CharField(max_length=200,null=True)
    deliverabels5 =  models.CharField(max_length=200,null=True)

    is_published =models.BooleanField(default=True)
    def __str__(self):
        return self.title



class Standard(models.Model):
    # portfolio = models.Foreignkey(Portfolio, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    deliverabels1 =  models.CharField(max_length=200,null=True)
    deliverabels2 =  models.CharField(max_length=200,null=True)
    deliverabels3 =  models.CharField(max_length=200,null=True)
    deliverabels4 =  models.CharField(max_length=200,null=True)
    deliverabels5 =  models.CharField(max_length=200,null=True)

    is_published =models.BooleanField(default=True)
    def __str__(self):
        return self.titleregister


class Premium(models.Model):
    # portfolio = models.Foreignkey(Portfolio, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    price = models.CharField(max_length=200)
    deliverabels1 =  models.CharField(max_length=200,null=True)
    deliverabels2 =  models.CharField(max_length=200,null=True)
    deliverabels3 =  models.CharField(max_length=200,null=True)
    deliverabels4 =  models.CharField(max_length=200,null=True)
    deliverabels5 =  models.CharField(max_length=200,null=True)

    is_published =models.BooleanField(default=True)
    def __str__(self):
        return self.title
