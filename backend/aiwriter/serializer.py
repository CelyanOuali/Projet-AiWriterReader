#serializer.py

from rest_framework import serializers
from . models import *

class ReactSerializer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['heroes', 'names', 'category', 'era', 'antiheroes', 'name', 'magic', 'science', 'stars', 'seas', 'side_characters', 'place', 'leadership']
        