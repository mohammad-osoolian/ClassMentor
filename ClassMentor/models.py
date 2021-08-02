from django.db import models

class form(models.Model):
    ostad = models.CharField(null=True, blank=True, max_length=255)
    tadris = models.IntegerField(null=True, blank=True)
    nomre = models.IntegerField(null=True, blank=True)
    akhlagh = models.IntegerField(null=True, blank=True)
    detailes = models.TextField(null=True, blank=True, max_length=255)

    def __str__(self):
        return self.ostad
    
class user(models.Model):
    username = models.CharField(null=True, blank=True , max_length=255)
    password = models.CharField(null=True, blank=True , max_length=255)
    name = models.CharField(null=True, blank=True , max_length=255)
    lastname = models.CharField(null=True, blank=True , max_length=255)

    def __str_(self):
        return self.username


