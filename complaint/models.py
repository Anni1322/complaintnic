from django.db import models

# Create your models here.
class User(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=30)
    image=models.ImageField(upload_to='images/profile_Images/',null=True,blank=True)
    def __str__(self):
        return str(self.name)

class Category(models.Model):    
    name = models.CharField(max_length=250,null=True, blank=True)

class TourPlace(models.Model):
    name = models.CharField(max_length=250,null=True, blank=True)
    description = models.CharField(max_length=250,null=True, blank=True)
    categoty_name =models.ForeignKey(to=Category,on_delete=models.CASCADE)
    image1 = models.ImageField(upload_to="Images/Dam/",null=True,blank=True)
    image2 = models.ImageField(upload_to="Images/Dam/",null=True,blank=True)
    image3 = models.ImageField(upload_to="Images/Dam/",null=True,blank=True)
    video1_link = models.CharField(max_length=1200,null=True, blank=True)
    video2_link = models.CharField(max_length=1200,null=True, blank=True)
    video3_link = models.CharField(max_length=1200,null=True, blank=True)
    video4_link = models.CharField(max_length=1200,null=True, blank=True)
    location = models.TextField(null=True, blank=True)
    popular = models.BooleanField()
    popular = models.BooleanField()