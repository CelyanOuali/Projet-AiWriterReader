#models.py

from django.db import models
from numpy import place

# Create your models here.
class React(models.Model):
    HERO_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('4', '4'),
    )
    heroes = models.CharField(max_length=1, choices=HERO_CHOICES, default='1')
    
    names = models.CharField(max_length=30, default='')
    
    CATEGORY_CHOICES = (
        ('Fantasy', 'Fantasy'),
        ('Science Fiction', 'Science Fiction'),
        ('Mystery', 'Mystery'), 
        ('Adventure', 'Adventure'),
    )
    category = models.CharField(max_length=30, choices=CATEGORY_CHOICES, default='')
    
    ERA_CHOICES = (
        ('Past', 'Past'),
        ('Present', 'Present'),
        ('Future', 'Future'), 
        ('Urban', 'Urban'),
        ('Prehistoric', 'Prehistoric'),
        ('Medieval', 'Medieval'),
    )
    era = models.CharField(max_length=15, choices=ERA_CHOICES, default='')
    
    antiheroes = models.BooleanField(default=False)
    
    name = models.CharField(max_length=30, default='')
    
    magic = models.BooleanField(default=False)
    
    science = models.BooleanField(default=False)
    
    stars = models.BooleanField(default=False)
    
    seas = models.BooleanField(default=False)
    
    SIDE_CHARACTERS_CHOICES = (
        ('0', '0'),
        ('1', '1'),
        ('2', '2'),
        ('4', '4'),
    )
    side_characters = models.CharField(max_length=1, choices=SIDE_CHARACTERS_CHOICES, default='0')
    
    place = models.CharField(max_length=30, default='')
    
    LEADERSHIP_CHOICES = (
        ('Monarchy', 'Monarchy'),
        ('Democracy', 'Democracy'),
        ('Anarchy', 'Anarchy'),
        ('Dictatorship', 'Dictatorship'),
        ('Managed Democracy', 'Managed Democracy'),
    )
    leadership = models.CharField(max_length=30, choices=LEADERSHIP_CHOICES, default='Monarchy')
    
    
    
    
    