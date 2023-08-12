from django.db import models


class Car(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    mileage = models.IntegerField()
    city = models.CharField(max_length=30)
    color = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} -> {self.city}'

