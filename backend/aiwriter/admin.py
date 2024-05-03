from django.contrib import admin
from .models import Story

class StoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'Construct_prompts', 'created_at')
    #list_display = ('heroes', 'names', 'category', 'era', 'antiheroes', 'name', 'magic', 'science', 'stars', 'seas', 'side_characters', 'place', 'leadership')
    
    readonly_fields= ('Construct_prompts',)
    
    
admin.site.register(Story, StoryAdmin)
