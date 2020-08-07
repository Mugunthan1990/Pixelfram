# Generated by Django 3.0.8 on 2020-08-03 05:22

from django.db import migrations, models
import embed_video.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('video', embed_video.fields.EmbedVideoField()),
                ('price', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
            ],
        ),
    ]
