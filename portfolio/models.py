from django.db import models
# from embed_video.fields import EmbedVideoField


# Create your models here.


class Portfolio(models.Model):
    # portfolio = models.Foreignkey(Portfolio, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    videolink = models.URLField(max_length = 200,null=True)
    # video = EmbedVideoField()
    # videofile= models.FileField(upload_to='img/', null=True, verbose_name="")
    # price = models.IntegerField()
    is_published =models.BooleanField(default=True)
    def __str__(self):
        return self.title
