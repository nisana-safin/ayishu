from django.db import models

# Create your models here.
from django.urls import reverse
from django.template.defaultfilters import slugify

class category(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    def get_url(self):
        return reverse('prod_cat',args=[self.slug])
class products(models.Model):
    def __str__(self):
        return self.name
    name=models.CharField(max_length=250,unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    image=models.ImageField(upload_to='products')
    desc=models.TextField()
    price=models.IntegerField()
    stock=models.IntegerField()
    available=models.BooleanField()
    categ=models.ForeignKey(category,on_delete=models.CASCADE)
    def get_url(self):
         return reverse('details',args=[self.categ.slug,self.slug])

