from tabnanny import verbose
from django.db import models

class Post(models.Model):
    class Meta:
        verbose_name='Post'
        verbose_name_plural='Post'
    Title=models.CharField(max_length=200)
    Text= models.TextField
    Author= models.ForeignKey
    Created_date= models.DateTimeField
    Published_date= models.DateTimeField