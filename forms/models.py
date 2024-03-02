from django.db import models

# Create your models here.

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    department = models.CharField(max_length=100)
    level = models.IntegerField()
    MEAL_CHOICES = (
    ('Beans and stew with bread/garri', 'Beans and stew with bread/garri'),
    ('Cereal and Bread', 'Cereal and Bread'),
    ('Sabath meal', 'Sabath meal'),
    ('Swallow and Ewedu soup', 'Swallow and Ewedu soup'),
    ('Swallow and Egusi soup', 'Swallow and Egusi soup'),
    ('Swallow and Okra soup', 'Swallow and Okra soup'),
    ('Fried rice', 'Fried rice'),
    ('Fried potato and Eggsauce', 'Fried potato and Eggsauce'),
    ('Jollef Rice', 'Jollef Rice'),
    ('Jollof Spaghetti', 'Jollof Spaghetti'),
    ('Moi Moi', 'Moi Moi'),
    ('Pap/custard/oats and Akara', 'Pap/custard/oats and Akara'),
    ('Plantain and Eggsauce', 'Plantain and Eggsauce'),
    ('Plantain and Stew', 'Plantain and Stew'),
    ('Porridge Beans', 'Porridge Beans'),
    ('Porridge Yam', 'Porridge Yam'),
    ('Spaghetti and Egg sauce', 'Spaghetti and Egg sauce'),
    ('Spaghetti and Stew', 'Spaghetti and Stew'),
    ('White rice and gbadun stew', 'White rice and gbadun stew'),
    ('White rice and red stew', 'White rice and red stew'),
    ('Yam and Egg sauce', 'Yam and Egg sauce'),
    ('Yam and Stew', 'Yam and Stew'),
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
