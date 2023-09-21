from django.db import models

# Create your models here.

class Destination(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='pictures')
    anons = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)

# class City(models.Model):
#     name = models.CharField(max_length=30)
#
#     class Meta:
#         verbose_name_plural = "cities"
#
#     def __str__(self):
#         return self.name