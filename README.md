# Skill Swap Platform

## Team
- **Kushal Yadav** *(Team Lead)* – [net.kushalyadav@gmail.com](mailto:net.kushalyadav@gmail.com)
- **Aditya Narayan Das** – [aditya123das123@gmail.com](mailto:aditya123das123@gmail.com)
- **Rahul Singh** – [rahulsingh51775177@gmail.com](mailto:rahulsingh51775177@gmail.com)
- **Laxman Prajapat** – [theprogrammer452023@gmail.com](mailto:theprogrammer452023@gmail.com)

## PROBLEM STATEMENT:

## Overview

Develop a Skill Swap Platform — a mini application that enables users to list their skills and request others in return.

## Features

- Basic info: Name, location (optional), profile photo (optional)
- List of skills offered
- List of skills wanted
- Availability (e.g., weekends, evenings)
- User can make their profile public or private
- Users can browse or search others by skill (e.g., “Photoshop” or “Excel”)
- Request & Accept Swaps:
  - Accept or reject swap offers
  - Show current and pending swap requests
  - Ratings or feedback after a swap
  - Users can delete pending swap requests

## 🔐 Admin Role

Platform moderators have access to:

- **Content Moderation**: Approve or reject inappropriate or spammy skill listings or messages.
- **User Management**: Ban users who violate community guidelines or misuse the platform.
- **Swap Oversight**:
  - View all swap requests (pending, accepted, rejected, or cancelled).
  - Monitor swap statistics and user activity.
- **Platform Communication**: Send platform-wide announcements such as feature updates or maintenance alerts.
- **Analytics & Reports**: Download user activity logs, feedback summaries, and detailed swap statistics.

## 🧠 Current Development Status

- ✅ **Backend**: Fully developed using Django & DRF with complete user authentication, profile, swap logic, and admin tools.
- ✅ **Frontend**: Built with React + Vite, includes login, registration, dashboard, and UI components.
- ✅ **Chatbot (Assistant)**: Integrated using OpenAI's API to assist users with queries and guidance.

> ⚠️ **Note**: Although all major components (frontend, backend, chatbot) are functional individually, we could not complete full integration due to time constraints during development.

## ⚙️ Tech Stack

- **Backend**: Django, Django REST Framework, Djoser (for auth), SQLite
- **Frontend**: React (Vite), TailwindCSS
- **Authentication**: JWT (SimpleJWT)
- **Dev Tools**: Thunder Client/Postman for API testing, Vite for hot reload
- **Other**: CORS, dotenv, Axios

## 🚀 Getting Started

### 📦 Backend Setup (Django)

```bash
cd backend
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
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

### 🔁 CORS Setup

In `settings.py`:

```python
CORS_ORIGIN_WHITELIST = [
    "http://localhost:5173",  # Vite
]
```

### 🔄 API Proxy for Vite

In `vite.config.js`, add:

```js
server: {
  proxy: {
    '/api': 'http://localhost:8000',
  },
},
```

## 📬 Contact

Made with collaboration and curiosity by [Kushal Yadav](https://www.linkedin.com/in/kushal-yadav-799310318/)
