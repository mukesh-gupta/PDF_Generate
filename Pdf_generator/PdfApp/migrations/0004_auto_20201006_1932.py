# Generated by Django 3.1.2 on 2020-10-06 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PdfApp', '0003_blog_created'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='img',
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='pics'),
        ),
        migrations.AddField(
            model_name='blog',
            name='logo',
            field=models.ImageField(default='static/emart.png', upload_to='logs'),
        ),
    ]
