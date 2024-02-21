from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    level = models.IntegerField()
    MEAL_CHOICES = (
        ('Beans and Stew', 'Beans and Stew'),
        ('Cereal and Bread', 'Cereal and Bread'),
        ('Cupcake', 'Cupcake'),
        ('Custard', 'Custard'),
        ('Eba', 'Eba'),
        ('Egusi soup', 'Egusi soup'),
        ('Fried rice', 'Fried rice'),
        ('Garri', 'Garri'),
        ('Fried potato and Eggsauce', 'Fried potato and Eggsauce'),
        ('Jollef Rice', 'Jollef Rice'),
        ('Jollef Spaghetti', 'Jollef Spaghetti'),
        ('Moi Moi', 'Moi Moi'),
        ('Okra soup', 'Okra soup'),
        ('Pap', 'Pap'),
        ('Plantain and Eggsauce', 'Plantain and Eggsauce'),
        ('Porrage Beans', 'Porrage Beans'),
        ('Porrage Yam', 'Porrage Yam'),
        ('Pounded yam', 'Pounded yam'),
        ('Semo', 'Semo'),
        ('Spaghetti and Egg sauce', 'Spaghetti and Egg sauce'),
        ('Spaghetti and Stew', 'Spaghetti and Stew'),
        ('Wheat Bread', 'Wheat Bread'),
        ('White rice and Gbadun', 'White rice and Gbadun'),
        ('White rice and Red stew', 'White rice and Red stew'),
        ('Yam and Egg sauce', 'Yam and Egg sauce'),
        ('Yam and Stew', 'Yam and Stew'),
        ('Zobo', 'Zobo'),
    )
    meal = models.CharField(max_length=100, choices=MEAL_CHOICES)
    RATING_CHOICES = (
        (1, 'Very poor'),
        (2, 'Poor'),
        (3, 'Fair'),
        (4, 'Good'),
        (5, 'Excellent'),
    )
    rating = models.IntegerField(choices=RATING_CHOICES)

    def __str__(self):
        return self.name  # Or any other field you want to use as the string representation
