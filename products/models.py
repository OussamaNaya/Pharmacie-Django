from django.db import models
from datetime import datetime


# Create your models here.

class Product(models.Model):
    x = [
        ('phone', 'phone'),
        ('computer', 'computer'),
    ]
    name = models.CharField(max_length=100, default='name', verbose_name='title')
    content = models.TextField(null=True, blank=True, verbose_name='description')
    price = models.DecimalField(max_digits=6, decimal_places=2, default=10.0)
    img = models.ImageField(upload_to='photos/%y/%m/%d', verbose_name='photo', default='home/photo1')
    quantite = models.IntegerField(default=0)
    new = models.BooleanField(default=True)
    #category = models.CharField(max_length=50, null=True, blank=True, choices=x)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Product'
        ordering = ['-name']


class Test(models.Model):
    date = models.DateField()
    time = models.TimeField(null=True)
    created = models.DateTimeField(default=datetime.now)
