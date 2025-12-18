from django.contrib import admin
from .models import Actualite


@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title', 'content', 'title_en', 'content_en']
    
    fieldsets = (
        ('Informations principales (Français)', {
            'fields': ('title', 'content', 'date', 'image')
        }),
        ('Traduction (Anglais)', {
            'fields': ('title_en', 'content_en'),
            'classes': ('collapse',),
        }),
    )
