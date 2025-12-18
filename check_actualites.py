#!/usr/bin/env python
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'master.settings')
django.setup()

from actualite.models import Actualite

print("=== Vérification des actualités ===\n")

actualites = Actualite.objects.all()
print(f"Nombre total d'actualités: {actualites.count()}\n")

for i, actualite in enumerate(actualites, 1):
    print(f"--- Actualité {i} (ID: {actualite.id}) ---")
    print(f"Titre FR: {actualite.title}")
    print(f"Titre EN: {actualite.title_en or '(vide)'}")
    print(f"Contenu FR (50 premiers caractères): {actualite.content[:50] if actualite.content else '(vide)'}...")
    print(f"Contenu EN (50 premiers caractères): {actualite.content_en[:50] if actualite.content_en else '(vide)'}...")
    print(f"Date: {actualite.date}")
    print()








