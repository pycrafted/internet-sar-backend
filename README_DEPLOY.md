# Guide de déploiement du backend Django

## Déploiement sur Render

### 1. Préparer le dépôt Git

Assurez-vous que votre code est sur GitHub, GitLab ou Bitbucket.

### 2. Créer un compte Render

1. Allez sur [render.com](https://render.com)
2. Créez un compte (gratuit)
3. Connectez votre dépôt Git

### 3. Créer une base de données PostgreSQL

1. Dans le dashboard Render, cliquez sur **"New +"** → **"PostgreSQL"**
2. Choisissez le plan **Free**
3. Notez les informations de connexion (elles seront utilisées automatiquement)

### 4. Créer un service Web

1. Cliquez sur **"New +"** → **"Web Service"**
2. Connectez votre dépôt Git
3. Configurez :
   - **Name** : `sar-backend` (ou le nom de votre choix)
   - **Region** : Choisissez la région la plus proche
   - **Branch** : `main` ou `master`
   - **Root Directory** : `backend`
   - **Runtime** : `Python 3`
   - **Build Command** : `./build.sh`
   - **Start Command** : `gunicorn master.wsgi:application --bind 0.0.0.0:$PORT`

### 5. Configurer les variables d'environnement

Dans les **Environment Variables** de votre service web, ajoutez :

```
SECRET_KEY=votre-secret-key-generee-aleatoirement
DEBUG=False
ALLOWED_HOSTS=votre-service.onrender.com
CORS_ALLOWED_ORIGINS=https://votre-frontend.vercel.app,https://votre-domaine.com
```

**Pour générer une SECRET_KEY :**
```python
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 6. Lier la base de données

1. Dans votre service web, allez dans **"Environment"**
2. Cliquez sur **"Link Database"**
3. Sélectionnez votre base de données PostgreSQL

La variable `DATABASE_URL` sera automatiquement ajoutée.

### 7. Déployer

1. Cliquez sur **"Create Web Service"**
2. Render va automatiquement :
   - Installer les dépendances
   - Exécuter les migrations
   - Collecter les fichiers statiques
   - Démarrer le serveur

### 8. Créer un superutilisateur

Une fois déployé, vous pouvez créer un superutilisateur via le shell :

1. Allez dans **"Shell"** de votre service
2. Exécutez :
```bash
python manage.py createsuperuser
```

### 9. Accéder à l'admin

Votre backend sera accessible à : `https://votre-service.onrender.com/admin/`

---

## Déploiement sur Railway

### 1. Créer un compte Railway

1. Allez sur [railway.app](https://railway.app)
2. Créez un compte avec GitHub

### 2. Créer un nouveau projet

1. Cliquez sur **"New Project"**
2. Sélectionnez **"Deploy from GitHub repo"**
3. Choisissez votre dépôt

### 3. Ajouter une base de données PostgreSQL

1. Cliquez sur **"New"** → **"Database"** → **"Add PostgreSQL"**
2. Railway créera automatiquement la base de données

### 4. Configurer le service

1. Railway détectera automatiquement Django
2. Configurez :
   - **Root Directory** : `backend`
   - **Start Command** : `gunicorn master.wsgi:application --bind 0.0.0.0:$PORT`

### 5. Variables d'environnement

Ajoutez dans **Variables** :
```
SECRET_KEY=votre-secret-key
DEBUG=False
ALLOWED_HOSTS=votre-service.railway.app
CORS_ALLOWED_ORIGINS=https://votre-frontend.vercel.app
```

---

## Important : Stockage des médias

⚠️ **Les fichiers uploadés (images) ne sont pas persistants sur les services gratuits.**

### Solutions recommandées :

1. **Cloudinary** (gratuit jusqu'à 25GB)
   - Service de gestion d'images
   - Intégration facile avec Django

2. **AWS S3** (payant mais très économique)
   - Stockage fiable et scalable
   - Intégration avec `django-storages`

3. **Cloudflare R2** (gratuit jusqu'à 10GB)
   - Compatible S3
   - Gratuit et performant

---

## Mise à jour du frontend

Une fois le backend déployé, mettez à jour l'URL de l'API dans votre frontend :

```env
NEXT_PUBLIC_API_URL=https://votre-backend.onrender.com
```

Ou dans `frontend/app/actualite/page.tsx` et `frontend/components/news-section.tsx`, changez :
```typescript
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'https://votre-backend.onrender.com'
```

---

## Support

Pour toute question, consultez :
- [Documentation Render](https://render.com/docs)
- [Documentation Railway](https://docs.railway.app)
- [Documentation Django Deployment](https://docs.djangoproject.com/en/5.2/howto/deployment/)

