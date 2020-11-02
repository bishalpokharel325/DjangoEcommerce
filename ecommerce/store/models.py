from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150, null=True, blank=True)
    price = models.FloatField()
    digital = models.BooleanField(default=True)
    image = models.ImageField(upload_to="")

    def __str__(self):
        return self.name
