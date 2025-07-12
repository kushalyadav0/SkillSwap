# Skill Swap Platform

# Team
- KushalYadav [Team Lead] [email](net.kushalyadav@gmail.com)
- Aaditya Narayanyan Das [email](aditya123das123@gmail.com)
- Rahul Singh [email](rahulsingh51775177@gmail.com)
- Laxman Prajapat [email](theprogrammer452023@gmail.com)
## PROBLEM STATEMENT: 

##Overview:

Develop a Skill Swap Platform — a mini application that enables users to list their skills and request others in return

## Features:

- Basic info: Name, location (optional), profile photo (optional)
- List of skills offered
- List of skills wanted
- Availability (e.g., weekends, evenings)
- User can make their profile public or private.
- Users can browse or search others by skill (e.g., “Photoshop” or “Excel”)
- Request & Accept Swaps:
- Accept or reject swap offers
- Show current and pending swap requests
- Ratings or feedback after a swap
- The user is also able to delete the swap request if it is not accepted.

## Admin Role
- Reject inappropriate or spammy skill descriptions.
- Ban users who violate platform policies.
- Monitor pending, accepted, or cancelled swaps.
- Send platform-wide messages (e.g., feature updates, downtime alerts).
- Download reports of user activity, feedback logs, and swap stats.

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
