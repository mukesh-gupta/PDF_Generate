# Generated by Django 3.1.2 on 2020-10-06 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PdfApp', '0004_auto_20201006_1932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='logo',
            field=models.ImageField(default='static/emart.png', upload_to='logos'),
        ),
    ]
