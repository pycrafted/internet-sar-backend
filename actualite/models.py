from django.db import models
from django.utils import timezone


class Actualite(models.Model):
    """Modèle pour les actualités de la SAR"""
    
    title = models.CharField(max_length=200, verbose_name="Titre")
    content = models.TextField(verbose_name="Contenu", help_text="Contenu complet de l'actualité")
    date = models.DateTimeField(verbose_name="Date de publication", default=timezone.now)
    image = models.ImageField(upload_to='actualites/', blank=True, null=True, verbose_name="Image")
    
    class Meta:
        verbose_name = "Actualité"
        verbose_name_plural = "Actualités"
        ordering = ['-date']
    
    def __str__(self):
        return self.title
