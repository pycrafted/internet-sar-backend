from rest_framework import serializers
from .models import Actualite


def get_localized_field(obj, field_fr, field_en, locale='fr'):
    """Retourne le champ localisé selon la langue"""
    if locale == 'en':
        # Essayer d'abord le champ anglais
        field_en_value = getattr(obj, field_en, None)
        if field_en_value and field_en_value.strip():  # Vérifier que le champ n'est pas vide
            return field_en_value
        # Fallback sur le français si l'anglais n'existe pas ou est vide
        return getattr(obj, field_fr)
    return getattr(obj, field_fr)


def format_date(obj, locale='fr', format_type='list'):
    """Formate la date selon la langue et le format"""
    if not obj.date:
        return ""
    
    if locale == 'en':
        months_en = {
            1: 'January', 2: 'February', 3: 'March', 4: 'April',
            5: 'May', 6: 'June', 7: 'July', 8: 'August',
            9: 'September', 10: 'October', 11: 'November', 12: 'December'
        }
        if format_type == 'list':
            return f"{obj.date.day} {months_en[obj.date.month]} {obj.date.year}"
        else:
            return f"{months_en[obj.date.month].lower()} {obj.date.year}"
    else:
        months_fr = {
            1: 'Janvier', 2: 'Février', 3: 'Mars', 4: 'Avril',
            5: 'Mai', 6: 'Juin', 7: 'Juillet', 8: 'Août',
            9: 'Septembre', 10: 'Octobre', 11: 'Novembre', 12: 'Décembre'
        }
        months_fr_lower = {
            1: 'janvier', 2: 'février', 3: 'mars', 4: 'avril',
            5: 'mai', 6: 'juin', 7: 'juillet', 8: 'août',
            9: 'septembre', 10: 'octobre', 11: 'novembre', 12: 'décembre'
        }
        if format_type == 'list':
            return f"{obj.date.day} {months_fr[obj.date.month]} {obj.date.year}"
        else:
            return f"{months_fr_lower[obj.date.month]} {obj.date.year}"


class ActualiteListSerializer(serializers.ModelSerializer):
    """Sérialiseur pour la liste des actualités (page d'accueil)"""
    
    # Formater la date au format "15 Janvier 2025"
    date = serializers.SerializerMethodField()
    # URL complète de l'image
    image = serializers.SerializerMethodField()
    # Titre localisé
    title = serializers.SerializerMethodField()
    
    class Meta:
        model = Actualite
        fields = ['id', 'title', 'date', 'image']
    
    def get_title(self, obj):
        """Retourne le titre selon la langue"""
        locale = self.context.get('locale', 'fr')
        return get_localized_field(obj, 'title', 'title_en', locale)
    
    def get_date(self, obj):
        """Formate la date au format '15 Janvier 2025'"""
        locale = self.context.get('locale', 'fr')
        return format_date(obj, locale, 'list')
    
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
    # Titre et contenu localisés
    title = serializers.SerializerMethodField()
    content = serializers.SerializerMethodField()
    
    class Meta:
        model = Actualite
        fields = ['id', 'title', 'content', 'date', 'image']
    
    def get_title(self, obj):
        """Retourne le titre selon la langue"""
        locale = self.context.get('locale', 'fr')
        return get_localized_field(obj, 'title', 'title_en', locale)
    
    def get_content(self, obj):
        """Retourne le contenu selon la langue"""
        locale = self.context.get('locale', 'fr')
        return get_localized_field(obj, 'content', 'content_en', locale)
    
    def get_date(self, obj):
        """Formate la date au format 'janvier 2025'"""
        locale = self.context.get('locale', 'fr')
        return format_date(obj, locale, 'detail')
    
    def get_image(self, obj):
        """Retourne l'URL complète de l'image"""
        if obj.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(obj.image.url)
            return obj.image.url
        return None

