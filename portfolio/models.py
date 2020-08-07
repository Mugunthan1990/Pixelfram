from django.db import models
from embed_video.fields import EmbedVideoField


# Create your models here.


class Portfolio(models.Model):
    # portfolio = models.Foreignkey(Portfolio, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    video = EmbedVideoField()
    price = models.IntegerField()
    is_published =models.BooleanField(default=True)
    def __str__(self):
        return self.title
