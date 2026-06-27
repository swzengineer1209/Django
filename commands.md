# Django + uv Setup Guide (Windows)

> **Requirements**
>
> * Windows 10/11
> * Python 3.14+
> * PowerShell

---

# 1. Check Python Installation

```powershell
python --version
```

Example:

```text
Python 3.14.6
```

---

# 2. Install uv (Recommended)

```powershell
powershell -ExecutionPolicy Bypass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Restart PowerShell after installation.

---

# 3. Verify uv Installation

```powershell
uv --version
```

Example:

```text
uv 0.11.25
```

If `uv` is not recognized, restart PowerShell or ensure:

```
C:\Users\<YourUsername>\.local\bin
```

is added to your **PATH**.

---

# 4. Navigate to Your Workspace

```powershell
cd D:\MERN\Django\DJANGO
```

Check your current directory:

```powershell
pwd
```

List files:

```powershell
dir
```

---

# 5. Create a New Project Folder

```powershell
mkdir MyDjangoProject
```

Move into it:

```powershell
cd MyDjangoProject
```

---

# 6. Initialize a uv Project

```powershell
uv init
```

This creates:

```
MyDjangoProject/
│
├── pyproject.toml
├── README.md
└── main.py
```

---

# 7. Create a Virtual Environment

```powershell
uv venv
```

Project structure:

```
MyDjangoProject/
│
├── .venv/
├── pyproject.toml
├── README.md
└── main.py
```

---

# 8. Activate the Virtual Environment

PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Command Prompt (CMD):

```cmd
.venv\Scripts\activate.bat
```

You should now see:

```text
(.venv)
```

at the beginning of your terminal.

---

# 9. Install Django

```powershell
uv add django
```

Verify:

```powershell
django-admin --version
```

---

# 10. Create a Django Project

```powershell
django-admin startproject config .
```

The `.` means **create the project in the current folder**.

---

# 11. Project Structure

```
MyDjangoProject/
│
├── .venv/
├── config/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── manage.py
├── pyproject.toml
├── uv.lock
└── README.md
```

---

# 12. Run the Development Server

```powershell
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

# 13. Create Your First App

```powershell
python manage.py startapp blog
```

Structure:

```
MyDjangoProject/
│
├── blog/
├── config/
├── manage.py
├── pyproject.toml
├── uv.lock
└── .venv/
```

---

# 14. Install Additional Packages

Example:

```powershell
uv add pandas
```

```powershell
uv add numpy
```

```powershell
uv add scikit-learn
```

Install multiple packages:

```powershell
uv add pandas numpy matplotlib plotly
```

---

# 15. Remove a Package

```powershell
uv remove pandas
```

---

# 16. Synchronize Dependencies

```powershell
uv sync
```

---

# 17. Run Python Using uv

```powershell
uv run python manage.py runserver
```

---

# 18. Deactivate Virtual Environment

```powershell
deactivate
```

---

# Daily Workflow

Open PowerShell:

```powershell
cd D:\MERN\Django\DJANGO\MyDjangoProject
```

Activate the environment:

```powershell
.venv\Scripts\Activate.ps1
```

Run the server:

```powershell
python manage.py runserver
```

When finished:

```powershell
deactivate
```

---

# Useful uv Commands

Check version:

```powershell
uv --version
```

Initialize project:

```powershell
uv init
```

Create virtual environment:

```powershell
uv venv
```

Install package:

```powershell
uv add <package-name>
```

Remove package:

```powershell
uv remove <package-name>
```

Synchronize packages:

```powershell
uv sync
```

Run Python:

```powershell
uv run python filename.py
```

---

# Useful Django Commands

Create project:

```powershell
django-admin startproject config .
```

Create app:

```powershell
python manage.py startapp app_name
```

Run server:

```powershell
python manage.py runserver
```

Create migrations:

```powershell
python manage.py makemigrations
```

Apply migrations:

```powershell
python manage.py migrate
```

Create superuser:

```powershell
python manage.py createsuperuser
```

Open Django shell:

```powershell
python manage.py shell
```

Collect static files:

```powershell
python manage.py collectstatic
```

Check project:

```powershell
python manage.py check
```

---

# Common PowerShell Commands

Current directory:

```powershell
pwd
```

List files:

```powershell
dir
```

Go to another directory:

```powershell
cd FolderName
```

Go back one directory:

```powershell
cd ..
```

Go directly to a folder:

```powershell
cd D:\MERN\Django\DJANGO
```

---

# Common Mistakes

### ❌ Wrong

```powershell
cd PS D:\MERN\Django\DJANGO>
```

### ❌ Wrong

```powershell
cd D:\MERN\Django\DJANGO>
```

### ✅ Correct

```powershell
cd D:\MERN\Django\DJANGO
```

**Remember:** The `PS ... >` text is the PowerShell prompt. Do **not** type it as part of your command.

---

# Complete Setup Workflow

```powershell
# Go to your workspace
cd D:\MERN\Django\DJANGO

# Create project
mkdir MyDjangoProject
cd MyDjangoProject

# Initialize uv
uv init

# Create virtual environment
uv venv

# Activate virtual environment
.venv\Scripts\Activate.ps1

# Install Django
uv add django

# Create Django project
django-admin startproject config .

# Run the development server
python manage.py runserver

# Create your first app
python manage.py startapp blog
```
