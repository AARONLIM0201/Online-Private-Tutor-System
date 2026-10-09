# Online Private Tutor System

This repository contains a Django web application for managing online tutoring workflows (accounts, bookings, sessions, chat, resources, and progress pages).

## Project structure

- `myproject.zip`: original submitted archive
- `myproject/`: extracted Django project
  - `manage.py`
  - `myproject/settings.py`
  - apps: `account`, `app`

## Installation and setup

Run these commands from the repository root:

```bash
# 1) Extract project files (already done in this repository)
unzip -o myproject.zip

# 2) Move into the Django project
cd myproject

# 3) Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
# .venv\Scripts\activate    # Windows PowerShell

# 4) Install dependencies
pip install "Django==4.1.4"

# 5) Apply migrations
python manage.py migrate

# 6) (Optional) Create admin user
python manage.py createsuperuser

# 7) Run development server
python manage.py runserver
```

Open the app at `http://127.0.0.1:8000/`.
Admin panel is available at `http://127.0.0.1:8000/admin/`.
