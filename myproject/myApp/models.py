from django.db import models

# Create your models here.
class GalleryModel(models.Model):
    image = models.ImageField(upload_to='images')
    name=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(self):
        return self.name


class RegisterModel(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    Phonenumber=models.CharField(max_length=20)
    address=models.TextField()

class Product(models.Model):
    gallery = models.ForeignKey(GalleryModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, null=False, blank=False) 
    product_image = models.ImageField(upload_to='images')