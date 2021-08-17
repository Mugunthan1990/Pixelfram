# Generated by Django 3.0.8 on 2021-08-17 05:24

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='moduleimage',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default='-', force_format=None, keep_meta=True, quality=100, size=[1080, 720], upload_to='rst/static/img/images'),
        ),
    ]
