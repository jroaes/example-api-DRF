from django.db import models


class Persona(models.Model):

    NOOB = 'noob'
    PRINCIPIANT = 'principiant'
    MODERATE = 'moderate'
    EXPERT = 'expert'

    CATEGORIES_CHOICES = (
        (NOOB, 'Noob'),
        (PRINCIPIANT, 'Principiant'),
        (MODERATE, 'Moderate'),
        (EXPERT, 'Expert'),
    )

    name = models.CharField(max_length=100)
    release_date = models.DateField()
    rating = models.IntegerField(default=0)
    category = models.CharField(max_length=10, choices=CATEGORIES_CHOICES)
