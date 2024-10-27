from django.db import models


class Buyer(models.Model):
    name = models.CharField(max_length=20)
    balance = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(decimal_places=1, max_digits=999)
    size = models.DecimalField(decimal_places=1, max_digits=999)
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='game')

    def __str__(self):
        return self.title
