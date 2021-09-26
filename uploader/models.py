from django.db import models
from django.db.models.fields import DateTimeField

# Create your models here.
class Image(models.Model):
    photo = models.ImageField(upload_to="myimage")
    date = DateTimeField(auto_now_add=True)