# Guide des Variables d'Environnement

## 🗄️ Base de données utilisée

**PostgreSQL** sera utilisée pour le déploiement sur Railway.

- Railway fournit automatiquement une base de données PostgreSQL
- La variable `DATABASE_URL` est ajoutée automatiquement par Railway
- SQLite est utilisé uniquement en développement local

---

## 🔗 Liaison Frontend Vercel ↔️ Backend Railway

**Non, ils ne sont pas automatiquement liés.** Vous devez configurer les variables d'environnement.

---

## 📋 Variables d'environnement à configurer

### 🚂 RAILWAY (Backend)

Dans votre service Railway, allez dans **Variables** et ajoutez :

```env
SECRET_KEY=django-insecure-remplacez-par-une-cle-secrete-generee-aleatoirement
DEBUG=False
ALLOWED_HOSTS=votre-service.railway.app
CORS_ALLOWED_ORIGINS=https://votre-frontend.vercel.app
```

**Note :** `DATABASE_URL` est ajoutée automatiquement par Railway quand vous créez une base PostgreSQL.

#### Comment générer une SECRET_KEY :

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Ou utilisez ce générateur en ligne : https://djecrety.ir/

---

### ⚡ VERCEL (Frontend)

Dans votre projet Vercel, allez dans **Settings** → **Environment Variables** et ajoutez :

```env
NEXT_PUBLIC_API_URL=https://votre-service.railway.app
```

**Important :** 
- Remplacez `votre-service.railway.app` par l'URL réelle de votre backend Railway
- Le préfixe `NEXT_PUBLIC_` est obligatoire pour que la variable soit accessible côté client

---

## 🔧 Étapes de configuration complète

### 1. Railway (Backend)

1. **Créer une base de données PostgreSQL :**
   - Dans Railway, cliquez sur **"New"** → **"Database"** → **"Add PostgreSQL"**
   - Railway créera automatiquement la base et ajoutera `DATABASE_URL`

2. **Configurer les variables d'environnement :**
   ```
   SECRET_KEY=votre-secret-key-generee
   DEBUG=False
   ALLOWED_HOSTS=votre-service.railway.app
   CORS_ALLOWED_ORIGINS=https://votre-frontend.vercel.app
   ```

3. **Configurer le service web :**
   - **Root Directory** : `backend`
   - **Start Command** : `python -m gunicorn master.wsgi:application --bind 0.0.0.0:$PORT`

4. **Notez l'URL de votre backend :**
   - Elle ressemble à : `https://votre-service.railway.app`

### 2. Vercel (Frontend)

1. **Ajouter la variable d'environnement :**
   - Allez dans **Settings** → **Environment Variables**
   - Ajoutez : `NEXT_PUBLIC_API_URL` = `https://votre-service.railway.app`
   - Sélectionnez tous les environnements (Production, Preview, Development)

2. **Redéployer :**
   - Vercel redéploiera automatiquement avec la nouvelle variable

---

## ✅ Vérification

### Backend Railway
Testez votre API :
```
https://votre-service.railway.app/api/actualites/
```

### Frontend Vercel
Vérifiez que le frontend charge les données depuis Railway en ouvrant la console du navigateur.

---

## 🔍 Dépannage

### Erreur CORS
Si vous voyez des erreurs CORS, vérifiez que :
- `CORS_ALLOWED_ORIGINS` dans Railway contient l'URL exacte de Vercel (avec `https://`)
- L'URL dans Vercel est correcte

### API non accessible
- Vérifiez que `ALLOWED_HOSTS` contient le domaine Railway
- Vérifiez que le service Railway est bien démarré

### Frontend ne charge pas les données
- Vérifiez la console du navigateur pour les erreurs
- Vérifiez que `NEXT_PUBLIC_API_URL` est bien configurée dans Vercel
- Redéployez le frontend après avoir ajouté la variable










