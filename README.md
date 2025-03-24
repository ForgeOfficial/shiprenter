# Technologies used:
- Server OS: Debian based (with apt packet manager)
- Coding languages: Python, HTML, CSS and JS
- Backend: Django
- Frontend: Django
- uWSGI: Gunicorn

<br>
<br>

# Installation:
## Development:
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
The ```railway.json``` configuration ensures full automation of the process

<br>
<br>

# Launch the website:
## Development:
```bash
sudo gunicorn --bind 127.0.0.1:8000 -t 200 --keep-alive 200 website.wsgi
```

## Production
The ```railway.json``` configuration ensures full automation of the process