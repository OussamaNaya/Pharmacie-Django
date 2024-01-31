from django.db import models

# Create your models here.

class Login(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

class Contact(models.Model):
    fn = models.CharField(max_length=255, null=True, blank=True)
    ln = models.CharField(max_length=255)
    eml = models.EmailField()
    sub = models.CharField(max_length=255)
    msg = models.TextField()

class Client(models.Model):
    fn = models.CharField(max_length=255, default='_oussama',null=True, blank=True)
    ln = models.CharField(max_length=255, default='_naya', null=True, blank=True)
    eml = models.EmailField(default='_o@gmail.com', null=True, blank=True)
    adr = models.CharField(max_length=255, default='_derb friha', null=True, blank=True)
    cont = models.CharField(max_length=255, default='_egypt', null=True, blank=True)
    post = models.IntegerField(default=0, null=True, blank=True)
    pho = models.CharField(max_length=20, default='_0777', null=True, blank=True)
    pas = models.CharField(max_length=255, default='_5555', null=True, blank=True)
    percentage_remis = models.IntegerField(default=0, null=True, blank=True)
    code_remis = models.IntegerField(auto_created= True,default=0)

    def __str__(self):
        return self.ln

class Commande(models.Model):
    fn = models.CharField(max_length=255, default='', null=True, blank=True)
    ln = models.CharField(max_length=255, default='', null=True, blank=True)
    eml = models.EmailField(default='_o@gmail.com', null=True, blank=True)
    p_name = models.CharField(default='', max_length=100, null=True, blank=True)

