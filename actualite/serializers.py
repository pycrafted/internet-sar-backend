from rest_framework import serializers
from .models import Actualite


class ActualiteListSerializer(serializers.ModelSerializer):
    """Sérialiseur pour la liste des actualités (page d'accueil)"""
    
    # Formater la date au format "15 Janvier 2025"
    date = serializers.SerializerMethodField()
    # URL complète de l'image
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Actualite
        fields = ['id', 'title', 'date', 'image']
    
    def get_date(self, obj):
        """Formate la date au format '15 Janvier 2025'"""
        months_fr = {
            1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril',
            5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
            9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'
        }
        if obj.date:
            return f"{obj.date.day} {months_fr[obj.date.month]} {obj.date.year}"
        return ""
    
    def get_image(self, obj):
        """Retourne l'URL complète de l'image"""
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None


class ActualiteDetailSerializer(serializers.ModelSerializer):
    """Sérialiseur pour les détails d'une actualité (page /actualite)"""
    
    # Formater la date au format "janvier 2025"
    date = serializers.SerializerMethodField()
    # URL complète de l'image
    image = serializers.SerializerMethodField()
    
    class Meta:
        model = Actualite
        fields = ['id', 'title', 'content', 'date', 'image']
    
    def get_date(self, obj):
        """Formate la date au format 'janvier 2025'"""
        months_fr = {
            1: 'janvier', 2: 'février', 3: 'mars', 4: 'avril',
            5: 'mai', 6: 'juin', 7: 'juillet', 8: 'août',
            9: 'septembre', 10: 'octobre', 11: 'novembre', 12: 'décembre'
        }
        if obj.date:
            return f"{months_fr[obj.date.month]} {obj.date.year}"
        return ""
    
    def get_image(self, obj):
        """Retourne l'URL complète de l'image"""
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

