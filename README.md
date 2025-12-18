# Backend Django - API Actualités SAR

## Installation

1. **Installer les dépendances** :
```bash
pip install -r requirements.txt
```

2. **Créer les migrations** :
```bash
python manage.py makemigrations
```

3. **Appliquer les migrations** :
```bash
python manage.py migrate
```

4. **Créer un superutilisateur** (optionnel, pour accéder à l'admin) :
```bash
python manage.py createsuperuser
```

5. **Lancer le serveur** :
```bash
python manage.py runserver
```

Le serveur sera accessible sur `http://localhost:8000`

## Endpoints API

### Liste des actualités (page /actualite)
```
GET http://localhost:8000/api/actualites/
```

### Actualités mises en avant (page d'accueil)
```
GET http://localhost:8000/api/actualites/?featured=true
```
ou
```
GET http://localhost:8000/api/actualites/featured/
```

### Détail d'une actualité
```
GET http://localhost:8000/api/actualites/{id}/
```

### Recherche
```
GET http://localhost:8000/api/actualites/?search=mot-clé
```

## Admin Django

Accéder à l'interface d'administration :
```
http://localhost:8000/admin/
```

Vous pouvez y créer, modifier et gérer les actualités.

## Structure des données

### Modèle Actualite
- `id` : Identifiant unique
- `title` : Titre de l'actualité
- `summary` : Résumé pour la page d'accueil
- `content` : Contenu complet
- `date` : Date de publication
- `image` : URL de l'image (optionnel)
- `created_at` : Date de création (automatique)
- `updated_at` : Date de modification (automatique)
- `is_featured` : Mise en avant sur la page d'accueil
- `is_published` : Publication (visible publiquement)











