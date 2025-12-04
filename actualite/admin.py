from django.contrib import admin
from .models import Actualite


@admin.register(Actualite)
class ActualiteAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title', 'content']
    
    fieldsets = (
        ('Informations principales', {
            'fields': ('title', 'content', 'date', 'image')
        }),
    )
