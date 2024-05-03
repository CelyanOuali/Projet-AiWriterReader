#views.py
#from rest_framework.decorators import action

from transformers import GPT2Tokenizer, GPT2LMHeadModel
from django.shortcuts import render

#La classe de base des viewsets fournit par défaut l'implémentation des opérations
# CRUD (Create, Read, Update, Delete). 
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import StorySerializer
from .models import Story
import random

#spécification de serializer_class et le queryset.
class StoryView(viewsets.ModelViewSet):
    serializer_class = StorySerializer
    queryset = Story.objects.all() #récupère l'ensemble des objets de la classe Story, sur lequel CRUD seront effectuées, dans la bdd
    
    
    def setup_gpt2(self):
        #initialisation du tokenizer et le modèle GPT-2
        self.tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
        self.model = GPT2LMHeadModel.from_pretrained("gpt2")
    
    def generate_story_from_prompt(self, prompt):
        try:
            input_ids = self.tokenizer.encode(prompt, return_tensors="pt")
            response = self.model.generate(input_ids, max_length=1000, do_sample=True)
            generated_story = self.tokenizer.decode(response[0], skip_special_tokens=True)
            return generated_story

        except Exception as e:
            raise RuntimeError(f"Failed to generate story: {str(e)}")
        
        
    def generate_user_prompt(self, request):
        # Récupérer les données de la requête POST
        data = request.data
        # Construire le prompt à partir des données reçues
        prompt = self.construct_prompt(data)
        try:
            # Générer l'histoire à partir du prompt
            generated_story = self.generate_story_from_prompt(prompt)
            return Response({"generated_story": generated_story})

        except Exception as e:
            return Response({"error": f"Failed to generate story: {str(e)}"}, status=500)

    
    def construct_prompt(self, data):
        # Appel à la méthode get_Construct_prompt définie dans models.py
        return Story.get_Construct_prompts(data)
    
    
    def generate_random_prompt(self, request):
        try:
            # Choisir aléatoirement parmi les prompts prédéfinis
            prompt = random.choice([
                "Once upon a time, in a land far, far away...",
                "In a galaxy not so far away, there was...",
                "Legend has it that in a distant kingdom...",
                "Once upon a midnight dreary, while I pondered, weak and weary..."
            ])
            # Générer l'histoire à partir du prompt choisi aléatoirement
            generated_story = self.generate_story_from_prompt(prompt)
            return Response({"generated_story": generated_story})

        except Exception as e:
            return Response({"error": f"Failed to generate story: {str(e)}"}, status=500)
        
        
    
    def display_story(self, request, story):
        #afficher l'histoire dans un modèle de page Django
        return render(request, 'story_template.html', {'story': story})
    
    
    
    def save_story(self, request):
        try:
            # Récupérer l'histoire à partir des données de la requête
            story = request.data.get('story', '')
            # Créer une instance de modèle Story et enregistrer l'histoire dans la base de données
            new_story = Story.objects.create(title="Titre de l'histoire", content=story)
            return Response({"message": "Story has been saved successfully.", "story_id": new_story.id}, status=201)

        except Exception as e:
            return Response({"error": f"Failed to save story: {str(e)}"}, status=500)


    # @action(detail=False, methods=['post'])
    # def generate_story(self, request):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
        
    #     # Récupérer les données du serializer
    #     validated_data = serializer.validated_data
        
    #     # Construire le prompt à partir des données reçues
    #     prompt = self.construct_prompt(validated_data)
        
    #     try:
    #         # Générer l'histoire à partir du prompt
    #         generated_story = self.generate_story_from_prompt(prompt)
    #         return Response({"generated_story": generated_story})

    #     except Exception as e:
    #         return Response({"error": f"Failed to generate story: {str(e)}"}, status=500)
    
    
    