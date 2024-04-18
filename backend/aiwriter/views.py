#views.py

from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from . serializer import *
from rest_framework.response import Response


class ReactView(APIView):
    
    serializer_class = ReactSerializer
    
    def construct_prompt(self, user_answers):
        prompt = ""
        questions = ['heroes', 'names', 'category', 'era', 'antiheroes', 'name', 'magic', 'science', 'stars', 'seas', 'side_characters', 'place', 'leadership']
        for i, (key, value) in enumerate(user_answers.items()):
            if key == "heroes":
                if value:
                    hero_count = len(value.split(', '))
                    prompt += f"They were {hero_count} heroes, named {value}, "
            elif key == "side_characters":
                if value:
                    side_character_count = int(value)
                    prompt += f"and {side_character_count} supporting characters, "
            elif key == "category":
                if value:
                    prompt += f"with a theme of {value.lower()}, "
            elif key == "era":
                if value:
                    prompt += f"set in the {value.lower()} era, "
            elif key == "antiheroes":
                if value == "Yes":
                    anti_hero_name = user_answers.get("name", "")
                    prompt += f"and there was an anti-hero named {anti_hero_name}, "
            elif key == "leadership":
                if value:
                    prompt += f"with a {value.lower()} type of leader, "
            else:
                if value == "True":
                    prompt += f"they {key.lower()}, "
        return prompt.strip() + "\n"
    
    #user_answers = {}
    
    def get(self, request):
        user_answers = request.query_params
        prompt = self.construct_prompt(user_answers)
        return Response({"prompt": prompt})
                    
        
        # output = [{"heroes": output.heroes, "names": output.names, "category": output.category, "era": output.era, "antiheroes": output.antiheroes, "name": output.name, "magic": output.magic, "science": output.science, "stars": output.stars, "seas": output.seas, "side_charcters": output.side_characters, "place": output.place, "leadership": output.leadership}
        #           for output in React.objects.all()]
        # return Response(output)
    
    def post(self, request):
        serializer = ReactSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            user_answers = request.data
            prompt = self.construct_prompt(user_answers)
            return Response({"prompt": prompt})


    
    
    