from django.db import models
from django.utils.timezone import datetime

# Create your models here.
class Blog(models.Model):
    name=models.CharField(max_length=250,blank=True)
    image=models.ImageField(upload_to='pics',blank=True)
    desc=models.TextField(max_length=500,blank=True)
    upload=models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        try:
            url = self.image.url

        except:
            url = ""
        return url

    @property
    def image_data(self):
        try:
            url=self.image.path
            url="B:/proj1/Pdf_generator/static/user-profile.png"

        except:
            url= "B:/proj1/Pdf_generator/static/user-profile.png"
        return url




