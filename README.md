# Lien du site:
[ShipRenter](shiprenter-production.up.railway.app)

<br>
<br>

# Technologies utilisées:
- OS du serveur: Basé sur Debian (avec gestionnaire de paquets apt)
- Serveur de déploiement: Railway
- Langages de codage: Python, HTML, CSS and JS
- Backend: Django
- Frontend: Django
- Base de donnée: PostgreSQL
- uWSGI: Gunicorn

<br>
<br>

# Résumé du fonctionnement:
Site de location de vaisseaux spatiaux utilisant Django pour gérer toute la logique et les pages côté serveur avec Tailwind CSS pour le design. Les utilisateurs parcourent les vaisseaux, cliquent pour voir les détails, et peuvent ajouter des vaisseaux à un panier géré par les sessions Django. Le site comprend aussi des pages d'informations standards.

<br>
<br>

# Installation:
## Développement:
```bash
sudo su
```
```bash
apt update && apt upgrade -y
```
```bash
apt install git -y
```
```bash
apt install python3 -y
```
```bash
apt install python3.12-venv
```
```bash
apt install pip -y
```
```bash
git clone git@github.com:ForgeOfficial/shiprenter.git
```
```bash
cd shiprenter
```
```bash
python3 -m venv venv
```
```bash
source venv/bin/activate
```
```bash
sudo pip install -r requirements.txt
```

## Production
La configuration ```railway.json``` assure une automatisation complète du processus

<br>
<br>

# Lancer le site Web:
## Développement:
```bash
sudo gunicorn --bind 127.0.0.1:8000 -t 200 --keep-alive 200 website.wsgi
```

## Production
La configuration ```railway.json``` assure une automatisation complète du processus