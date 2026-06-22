# Email Signature Generator — Django Project

A simple Django web app that serves the Victoria Finance email signature generator.

## Project Structure

```
email_sig/
├── manage.py
├── requirements.txt
├── README.md
├── email_sig/               ← Django project package
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── signature_app/           ← The signature generator app
    ├── __init__.py
    ├── apps.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── signature_app/
            └── generator.html
```

## Setup & Run

### 1. Create and activate a virtual environment

```bash
python -m venv venv

# On Windows:
venv\Scripts\activate

# On macOS/Linux:
source venv/bin/activate
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the development server

```bash
python manage.py runserver
```

### 4. Open in your browser

Visit: http://127.0.0.1:8000/

---

## Deploying to Production

Before going live, update `settings.py`:

1. Change `SECRET_KEY` to a strong random value
2. Set `DEBUG = False`
3. Set `ALLOWED_HOSTS` to your actual domain, e.g. `['yourdomain.co.tz']`
4. Run `python manage.py collectstatic` and configure your web server (Nginx + Gunicorn recommended)
