#models.py

from django.db import models
#from numpy import place
from django.db.models.signals import pre_save
from django.dispatch import receiver
#from .serializers import StorySerializer
from django.utils import timezone


# Create your models here.
class Story(models.Model):
    
    title = models.CharField(max_length=120, default='')
    
    
    HERO_CHOICES = (
        ('1', '1'),
        ('2', '2'),
        ('3', '3'),
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
        ('3', '3'),
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
    
    
    Construct_prompts = models.CharField(max_length=120, default='', editable=False)
    
    
    created_at = models.DateTimeField(default=timezone.now)
    
    
    def get_Construct_prompts(self):
        prompt=""
        if int(self.heroes) > 0:
            hero_count = int(self.heroes)
            prompt += f"They were {hero_count} heroes, named {self.names}, "
        
        if int(self.side_characters) > 0:
            side_character_count = int(self.side_characters)
            prompt += f"and {side_character_count} supporting characters, "
        
        if self.category:
            prompt += f"with a theme of {self.category.lower()}, "
        
        if self.era:
            prompt += f"set in the {self.era.lower()} era, "
        
        if self.antiheroes:
            if self.antiheroes == True:
                prompt += f"and there was an anti-hero named {self.name}, "
        
        if self.leadership:
            prompt += f"with a {self.leadership.lower()} type of leader, "
        
        if self.magic == True:
                prompt += f"they use magic, "
        
        if self.science == True:
                prompt += f"they are advanced in science, "
                
        if self.stars == True:
                prompt += f"they explore stars, "
        
        if self.seas == True:
                prompt += f"they explore seas, "
                
        return prompt
    
    
    def __str__(self):
        return self.title


@receiver(pre_save, sender=Story)
def update_generated_by_prompts(sender, instance, **kwargs):
    if not instance.pk:  # Vérifie si l'instance est nouvellement créée
        instance.Construct_prompts = instance.get_Construct_prompts()  # Affecte le titre au champ Story_generated_by_prompts
    


# @receiver(pre_save, sender=Story)
# def generate_story_on_save(sender, instance, **kwargs):
#     if not instance.pk:  # Vérifie si l'instance est nouvellement créée
#         # Construire le prompt à partir des données de l'instance
#         instance.Construct_prompts = instance.get_Construct_prompts()
        
#         try:
#             # Générer l'histoire à partir du prompt
#             generated_story = instance.generate_story_from_prompt(instance.Construct_prompts)
#             # Sauvegarder l'histoire générée dans l'instance de Story
#             instance.generated_story = generated_story

#         except Exception as e:
#             # En cas d'erreur lors de la génération de l'histoire, imprimez l'erreur
#             print(f"Failed to generate story: {str(e)}")
    
    
    
    