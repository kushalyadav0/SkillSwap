# 🌀 Django + React Boilerplate

This is a minimal boilerplate project that integrates a **Django backend** with a **React frontend**. Designed for rapid development, this setup allows you to build full-stack web applications efficiently.

---

## 📁 Project Structure

```
Django-React-Boilerplate/
├── backend/ # Django backend
│ └── manage.py
├── frontend/ # React frontend (Vite/CRA)
│ └── package.json
├── .gitignore
├── README.md
└── requirements.txt
```

---

## 🚀 Features

- 🔗 Django REST Framework for API development
- ⚛️ React frontend with Vite or Create React App
- 🛡️ CORS support for seamless communication
- 📦 Modern package management (npm + pip)
- 🔄 Hot reloading in development

---

## 🛠️ Getting Started

### 🔧 Prerequisites

- Python 3.10+
- Node.js & npm
- Virtual environment (recommended)

---

### 📦 Backend Setup (Django)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### ⚛️ Frontend Setup (React)

```bash
cd frontend
npm install
npm run dev
```

### 🔄 Proxy API (Vite/CRA Config)
Ensure your React frontend proxies API requests to Django:

```
// vite.config.js or package.json (CRA)
server: {
  proxy: {
    '/api': 'http://localhost:8000',
  }
}
```

### 🧪 Development Tips
Update CORS settings in settings.py:

```
CORS_ORIGIN_WHITELIST = [
    "http://localhost:3000",  # React
]
```
- API base path: /api/ (you can change this in your URLs)

- Use axios or fetch to call the API from React

### 🙌 Acknowledgements
Inspired by Django REST + React best practices.

### 📬 Contact
Built by [Kushal Yadav](https://www.linkedin.com/in/kushal-yadav-799310318/)