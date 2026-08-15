# 🔗 Shortify — URL Shortener

<p align="center">
  <img src="https://img.shields.io/badge/Shortify-URL%20Shortener-6366f1?style=for-the-badge&logo=link&logoColor=white" alt="Shortify" />
  <img src="https://img.shields.io/badge/Django-6.1-092e20?style=for-the-badge&logo=django&logoColor=white" alt="Django" />
  <img src="https://img.shields.io/badge/PostgreSQL-Database-4169e1?style=for-the-badge&logo=postgresql&logoColor=white" alt="PostgreSQL" />
</p>

<p align="center">
  <strong>A simple, modern, and professional URL shortening application built with Django and PostgreSQL.</strong>
</p>

<p align="center">
  Create short links, manage your URLs, track clicks, and access your link analytics through a clean, unified dashboard.
</p>

---

## 📸 Project Preview

<p align="center">
  <img src="assets/screenshots/home.png" alt="Shortify Home" width="900" />
</p>

<p align="center">
  <em>Shortify — Home Page Preview</em>
</p>

---

## ✨ Features

### 🔗 URL Shortening
* Convert long URLs into short, easy-to-share links.
* Automatically generate unique short codes.
* One-click copying for generated short URLs.

### 📊 Dashboard
* View all shortened URLs in a single overview.
* Fast dynamic search functionality for existing links.
* Aggregated metrics for total links created and overall click counts.
* Quick actions to manage or inspect individual links.

### 👁️ Link Details
* Display comprehensive metadata for any shortened URL.
* Access original destination links, generated codes, and target redirects.
* View total click stats and precise creation/update timestamps.
* Direct action controls: copy link or test redirection in a new tab.

### 🗑️ Link Management
* Safely remove obsolete or invalid links.
* Built-in deletion confirmation flow.
* Automatic cascade clean-up of associated database records.

### 🎨 Modern UI
* Clean, responsive interface built with Bootstrap Icons and card layouts.
* Mobile-first responsive navigation and viewing experience.

---

## 🖥️ Screenshots

### 🏠 Home Page
<p align="center">
  <img src="assets/screenshots/home.png" alt="Shortify Home Page" width="900" />
</p>

The main entry point where users submit target URLs to instantly generate unique shortened links.

---

### 📊 Dashboard
<p align="center">
  <img src="assets/screenshots/dashboard.png" alt="Shortify Dashboard" width="900" />
</p>

The central management interface providing searchable lists, total link count statistics, total click performance metrics, and quick management options.

---

### 🔍 Link Details
<p align="center">
  <img src="assets/screenshots/detail.png" alt="Shortify Link Details" width="900" />
</p>

Detailed breakdown page offering complete historical timestamps, click analytical data, direct testing triggers, and deletion actions.

---

## 🛠️ Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **Python** | Primary backend language |
| **Django** | Web framework & ORM layer |
| **PostgreSQL** | Production-ready relational database |
| **HTML5 / CSS3** | Structural design and responsive layouts |
| **JavaScript** | Dynamic client-side interactions and clipboard functions |
| **Bootstrap Icons** | Scalable UI iconography |

---

## 🏗️ Project Architecture

```text
Shortify/
│
├── manage.py
│
├── shortify/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
│
├── links/
│   ├── migrations/
│   │   └── __init__.py
│   ├── templates/
│   │   └── links/
│   │       ├── base.html
│   │       ├── home.html
│   │       ├── dashboard.html
│   │       └── detail.html
│   ├── static/
│   │   └── links/
│   │       ├── css/
│   │       │   └── style.css
│   │       └── js/
│   │           └── app.js
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
│
├── assets/
│   └── screenshots/
│       ├── home.png
│       ├── dashboard.png
│       └── detail.png
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt


### 🔄 How Shortify Works

```text
       User
        │
        ▼
 Enter Long URL
        │
        ▼
   Django Form
        │
        ▼
   Validate URL
        │
        ▼
Generate Short Code
        │
        ▼
    PostgreSQL ◄──── (Save ShortURL Model)
        │
        ▼
Short URL Created
        │
        ▼
 ┌─────────────┐
 │ Short Link  │
 └──────┬──────┘
        │
        ▼
 User Opens Link
        │
        ▼
Django Redirect View ───► Increment Click Count
        │
        ▼
Original Destination

```

---

## ⚙️ Requirements

Before running the project, make sure you have the following installed:

* **Python 3.11+**
* **PostgreSQL**
* **pip**
* **Git**

Verify your local installation:

```bash
python --version
pip --version
psql --version

```

---

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone [https://github.com/SamirPokhrel/Shortify.git](https://github.com/SamirPokhrel/Shortify.git)
cd Shortify

```

### 2. Set Up Virtual Environment

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

```

> *If PowerShell blocks execution scripts, run:* `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`

**Linux / macOS:**

```bash
python3 -m venv venv
source venv/bin/activate

```

### 3. Install Dependencies

```bash
pip install -r requirements.txt

```

---

## 🗄️ PostgreSQL Configuration

1. Create a local PostgreSQL database:
```sql
CREATE DATABASE shortify;

```


2. Update database credentials in `shortify/settings.py`:
```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "shortify",
        "USER": "postgres",
        "PASSWORD": "your_password",
        "HOST": "localhost",
        "PORT": "5432",
    }
}

```



---

## 🧱 Database Migrations & Admin Setup

Apply database migrations:

```bash
python manage.py makemigrations
python manage.py migrate

```

Create an admin account:

```bash
python manage.py createsuperuser

```

---

## ▶️ Running the Application

Start the development server:

```bash
python manage.py runserver

```

Access the application in your browser:

* **Home Page:** [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* **Dashboard:** [http://127.0.0.1:8000/dashboard/](http://127.0.0.1:8000/dashboard/)
* **Admin Panel:** [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

---

## 🔗 URL Routing Reference

| Endpoint | Method | Description |
| --- | --- | --- |
| `/` | `GET / POST` | Home page & link creation form |
| `/dashboard/` | `GET` | Main management dashboard |
| `/link/<short_code>/` | `GET` | Detailed statistics & management actions for a link |
| `/<short_code>/` | `GET` | Redirect trigger to destination URL (increments click counter) |
| `/admin/` | `GET / POST` | Django administration panel |

*Example short link resolution:* `http://127.0.0.1:8000/qYAp1x/` maps `qYAp1x` directly to its targeted original destination.

---

## 📊 Core Data Model

The core URL processing engine relies on the `ShortURL` model structure:

```text
ShortURL
├── original_url : URLField
├── short_code   : CharField (Unique)
├── clicks       : PositiveIntegerField
├── created_at   : DateTimeField
└── updated_at   : DateTimeField

```

### Model Schema

| Field | Data Type | Description |
| --- | --- | --- |
| `original_url` | `URLField` | Targeted destination web address |
| `short_code` | `CharField` | Unique auto-generated alphanumeric identifier |
| `clicks` | `PositiveIntegerField` | Cumulative access counter |
| `created_at` | `DateTimeField` | Record creation timestamp |
| `updated_at` | `DateTimeField` | Timestamp of last modification |

---

## 🔐 Security Considerations

Shortify implements native Django security standards:

* **CSRF Protection:** Secure cross-site request forgery tokens on form inputs.
* **ORM Query Parameterization:** Automatic SQL injection prevention.
* **Form Validation:** Input scrubbing and standard URL structure checks.
* **Password Hashing:** PBKDF2 hashing for administrative access control.

> ⚠️ **Production Note:** Ensure sensitive properties (`SECRET_KEY`, `DATABASE_PASSWORD`, and `DEBUG = False`) are served via environment variables in production setups.

---

## 🧪 Development Commands

Check system setup for potential errors:

```bash
python manage.py check

```

Open interactive Django shell:

```bash
python manage.py shell

```

Collect static assets for production deployments:

```bash
python manage.py collectstatic

```

---

## 📦 Key Dependencies

Managed via `requirements.txt`:

```text
Django>=6.0
psycopg[binary]

```

Re-install anytime using:

```bash
pip install -r requirements.txt

```

---

## 🛣️ Future Roadmap

* [ ] 👤 User authentication and personalized account workspaces
* [ ] 🔐 Private and password-protected short links
* [ ] 🏷️ Custom slug aliases (e.g., `/my-custom-name`)
* [ ] 📈 Advanced geographic, device, and browser analytics
* [ ] 🏷️ QR code generator integration
* [ ] ⌛ Link expiration dates
* [ ] 🌐 Public REST API endpoints with rate-limiting
* [ ] ⚡ Caching optimization using Redis
* [ ] 🐳 Full Docker setup & docker-compose support

---

## 🎯 Learning Objectives

This project was built to practice core full-stack software development workflows:

* **Architecture:** Organizing modular Django applications and template inheritance.
* **Database Management:** Designing PostgreSQL schemas, writing Django ORM queries, and handling migrations.
* **Frontend-Backend Integration:** Managing state from templates down to controllers and database operations.
* **UX/UI Design:** Translating web component concepts into accessible dashboard interfaces.

---

## 📌 Project Status

🟢 **Active Development** — Core functionality is complete and ready for feature extensions like authentication, caching, and cloud deployments.

---

## 👨‍💻 Author

**Samir Pokhrel**

*Bachelor of Science in Computer Science and Information Technology*

---

## 📄 License

This project is open source and available under the terms specified in the [LICENSE](https://github.com/pokhrelsamir/Shortify/blob/main/LICENSE) file.