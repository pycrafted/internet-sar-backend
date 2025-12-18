#!/usr/bin/env python
"""
Script pour ajouter des traductions anglaises aux actualités existantes.
Vous pouvez modifier les traductions dans l'admin Django après.
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'master.settings')
django.setup()

from actualite.models import Actualite

print("=== Ajout de traductions anglaises aux actualités ===\n")

actualites = Actualite.objects.all()

# Traductions de base (vous pouvez les modifier dans l'admin Django après)
translations = {
    3: {
        'title_en': 'Africa Energy Week: SAR highlights Senegal\'s expertise',
        'content_en': 'Africa Energy Week 2025: The African Refining Company (SAR) alongside the Ministry of Energy, Petroleum and Mines.\n\nA week rich in meetings, exchanges and sharing of experiences, around the challenges and opportunities of the African energy sector.\n\nIntervention by General Manager Abib DIOP, Strategy HEC Paris in the panel: "Invest in Senegal" and that of Executive Director Operations Daouda Kebe in the panel: "Value Addition Scaling Africa\'s Refining Capacity to fuel African industries".'
    },
    2: {
        'title_en': 'SAR participates in the Invest In Senegal Forum',
        'content_en': 'The African Refining Company (SAR) participates in the Invest In Senegal Forum to promote investment opportunities in the Senegalese energy sector.'
    },
    1: {
        'title_en': 'SAR participates in JCL 2025 and strengthens its commitment to the national economy',
        'content_en': 'Historical and strategic player in the Senegalese energy sector, the African Refining Company (SAR) participates in the 2025 Senegal Business Days (JCL) and reinforces its commitment to the national economy.'
    }
}

for actualite in actualites:
    if actualite.id in translations:
        trans = translations[actualite.id]
        actualite.title_en = trans['title_en']
        actualite.content_en = trans['content_en']
        actualite.save()
        print(f"✓ Actualité {actualite.id} traduite: {actualite.title_en[:50]}...")
    else:
        print(f"⚠ Actualité {actualite.id} n'a pas de traduction définie dans le script")

print("\n=== Vérification ===")
for actualite in actualites:
    print(f"ID {actualite.id}: EN={'✓' if actualite.title_en else '✗'}")

print("\n✓ Terminé! Vous pouvez maintenant voir les traductions sur /en/actualite")
print("Note: Vous pouvez modifier les traductions dans l'admin Django: /admin/actualite/actualite/")








