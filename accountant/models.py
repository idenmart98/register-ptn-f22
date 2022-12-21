from django.db import models

from profile_app.models import User 


class Category(models.Model):
    name = models.CharField(max_length=50 , verbose_name='Name')


class Note(models.Model):
    name = models.CharField(verbose_name='Name' , max_length=50)
    price = models.DecimalField(max_digits=6 , decimal_places=2)
    category = models.ForeignKey(Category , on_delete=models.CASCADE , related_name='notes')
    user = models.ForeignKey(User , on_delete=models.CASCADE , related_name='notes')
    created = models.DateTimeField(auto_now_add=True)