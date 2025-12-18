from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.db.models import Q
from .models import Actualite
from .serializers import ActualiteListSerializer, ActualiteDetailSerializer


class ActualiteViewSet(viewsets.ReadOnlyModelViewSet):
    """
    ViewSet pour les actualités.
    ReadOnly car on ne permet que la lecture (GET) pour l'instant.
    """
    queryset = Actualite.objects.all()
    serializer_class = ActualiteDetailSerializer
    
    def get_serializer_class(self):
        """Utilise le bon sérialiseur selon l'action"""
        if self.action == 'list' and self.request.query_params.get('featured') == 'true':
            return ActualiteListSerializer
        elif self.action == 'list':
            return ActualiteDetailSerializer
        return ActualiteDetailSerializer
    
    def get_queryset(self):
        """Filtre les actualités selon les paramètres de requête"""
        queryset = Actualite.objects.all()
        
        # Recherche par mot-clé (dans les deux langues)
        search = self.request.query_params.get('search', None)
        if search:
            locale = self.request.query_params.get('locale', 'fr')
            if locale == 'en':
                queryset = queryset.filter(
                    Q(title_en__icontains=search) |
                    Q(content_en__icontains=search) |
                    Q(title__icontains=search) |  # Fallback sur le français si l'anglais n'existe pas
                    Q(content__icontains=search)
                )
            else:
                queryset = queryset.filter(
                    Q(title__icontains=search) |
                    Q(content__icontains=search) |
                    Q(title_en__icontains=search) |  # Recherche aussi en anglais
                    Q(content_en__icontains=search)
                )
        
        return queryset.order_by('-date')
    
    def get_serializer_context(self):
        """Ajoute le request et la locale au contexte pour les URLs d'images et la traduction"""
        context = super().get_serializer_context()
        context['request'] = self.request
        
        # Récupérer la langue depuis les paramètres de requête ou le header Accept-Language
        locale = self.request.query_params.get('locale', None)
        if not locale:
            # Essayer de détecter depuis le header Accept-Language
            accept_language = self.request.META.get('HTTP_ACCEPT_LANGUAGE', '')
            if 'en' in accept_language.lower():
                locale = 'en'
            else:
                locale = 'fr'
        
        # Debug: logger la locale utilisée
        import logging
        logger = logging.getLogger(__name__)
        logger.info(f"ActualiteViewSet: Using locale '{locale}' (from query param: {self.request.query_params.get('locale', 'None')})")
        
        context['locale'] = locale
        return context
