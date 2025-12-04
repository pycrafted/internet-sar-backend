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
        
        # Recherche par mot-clé
        search = self.request.query_params.get('search', None)
        if search:
            queryset = queryset.filter(
                Q(title__icontains=search) |
                Q(content__icontains=search)
            )
        
        return queryset.order_by('-date')
    
    def get_serializer_context(self):
        """Ajoute le request au contexte pour les URLs d'images"""
        context = super().get_serializer_context()
        context['request'] = self.request
        return context
