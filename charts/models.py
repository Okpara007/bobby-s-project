from django.db import models

# Create your models here.

class Chart(models.Model):
    meal = models.CharField(max_length=200)
    rating_amount = models.IntegerField()

    def __str__(self):
        return "{}-{}".format(self.meal, self.rating_amount)