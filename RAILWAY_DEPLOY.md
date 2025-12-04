# Guide de déploiement Railway - Résolution des problèmes

## Problème : `gunicorn: command not found`

### Solution 1 : Utiliser `python -m gunicorn` (Recommandé)

Dans Railway, configurez la **Start Command** comme suit :

```bash
python -m gunicorn master.wsgi:application --bind 0.0.0.0:$PORT
```

### Solution 2 : Configuration dans Railway Dashboard

1. Allez dans votre service sur Railway
2. Cliquez sur **Settings**
3. Dans **Deploy**, configurez :
   - **Root Directory** : `backend`
   - **Start Command** : `python -m gunicorn master.wsgi:application --bind 0.0.0.0:$PORT`
   - **Build Command** : `pip install -r requirements.txt && python manage.py collectstatic --no-input`

### Solution 3 : Utiliser le fichier railway.json

Railway détectera automatiquement le fichier `railway.json` à la racine du projet.

### Solution 4 : Variables d'environnement requises

Assurez-vous d'avoir configuré ces variables dans Railway :

```
SECRET_KEY=votre-secret-key-generee
DEBUG=False
ALLOWED_HOSTS=votre-service.railway.app
CORS_ALLOWED_ORIGINS=https://votre-frontend.vercel.app
```

### Solution 5 : Base de données PostgreSQL

1. Créez une base de données PostgreSQL dans Railway
2. Railway ajoutera automatiquement la variable `DATABASE_URL`
3. Assurez-vous que `dj-database-url` est dans `requirements.txt` (déjà présent)

## Vérification

Après le déploiement, vérifiez que :
1. Les migrations sont appliquées
2. Le serveur démarre sans erreur
3. L'API est accessible à `https://votre-service.railway.app/api/actualites/`

## Commandes utiles

Pour créer un superutilisateur après déploiement :
```bash
railway run python manage.py createsuperuser
```

Pour voir les logs :
```bash
railway logs
```

