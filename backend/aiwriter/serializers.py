#serializers: convertir les instances de modèle en JSON (données sous forme clé-valeur, en objet et tableau)
#afin que le frontend puisse travailler avec les données reçues.

from rest_framework import serializers
from .models import Story

#Spécification du modèle avec lequel travailler et les champs à convertir en JSON.
class StorySerializer(serializers.ModelSerializer):
    Construct_prompts = serializers.SerializerMethodField()

    class Meta:
        model = Story
        fields = ('id', 'title', 'heroes', 'names', 'category', 'era', 'antiheroes', 'name', 'magic', 'science', 'stars', 'seas', 'side_characters', 'place', 'leadership', 'Construct_prompts')


    def get_Construct_prompts(self, obj):
        prompt=""
        if int(obj.heroes) > 0:
            hero_count = int(obj.heroes)
            prompt += f"They were {hero_count} heroes, named {obj.names}, "
        
        if int(obj.side_characters) > 0:
            side_character_count = int(obj.side_characters)
            prompt += f"and {side_character_count} supporting characters, "
        
        if obj.category:
            prompt += f"with a theme of {obj.category.lower()}, "
        
        if obj.era:
            prompt += f"set in the {obj.era.lower()} era, "
        
        if obj.antiheroes:
            if obj.antiheroes == True:
                prompt += f"and there was an anti-hero named {obj.name}, "
        
        if obj.leadership:
            prompt += f"with a {obj.leadership.lower()} type of leader, "
        
        if obj.magic == True:
                prompt += f"they use magic, "
        
        if obj.science == True:
                prompt += f"they are advanced in science, "
                
        if obj.stars == True:
                prompt += f"they explore stars, "
        
        if obj.seas == True:
                prompt += f"they explore seas, "
                
        return prompt
        
        