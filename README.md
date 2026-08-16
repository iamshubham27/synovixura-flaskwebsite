<div align="center">

# ✦ SYNOVIXURA

### **Where Technology Meets Design**

A modern, immersive technology website built with **Flask, Supabase & JavaScript** — redesigned from the ground up with a clean Bento-inspired interface, dark aesthetics, smooth interactions, and a production deployment on Render.

<br/>

<a href="https://synovixura-website-flsk.onrender.com">
  <img src="https://img.shields.io/badge/%E2%9C%A6_Live_Demo-Synovixura-000000?style=for-the-badge&logo=render&logoColor=white" alt="Live Demo"/>
</a>
<a href="https://github.com/iamshubham27/synovixura-flaskwebsite">
  <img src="https://img.shields.io/badge/Source_Code-GitHub-181717?style=for-the-badge&logo=github" alt="GitHub"/>
</a>

<br/><br/>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Flask-Backend-000000?style=flat-square&logo=flask&logoColor=white"/>
<img src="https://img.shields.io/badge/Supabase-Database-3ECF8E?style=flat-square&logo=supabase&logoColor=white"/>
<img src="https://img.shields.io/badge/JavaScript-Frontend-F7DF1E?style=flat-square&logo=javascript&logoColor=black"/>
<img src="https://img.shields.io/badge/Render-Deployed-46E3B7?style=flat-square&logo=render&logoColor=black"/>

<br/><br/>

> **Aesthetic interface. Practical architecture. Full-stack execution.**

</div>

---

## ◈ Overview

**Synovixura** is a modern technology-focused web application created to combine a visually striking frontend with a lightweight Python backend.

The project preserves the original **Synovixura** visual language — including the Bento-style layout, dark interface, dashboard previews, animations and interactive components — while migrating the backend architecture to **Flask + Supabase**.

The result is a complete full-stack application that can be developed locally and deployed as a production web service.

### ✦ What makes it interesting?

* ◈ Modern **Bento Grid** inspired UI
* ◈ Dark, minimal and futuristic visual language
* ◈ Smooth interactive frontend
* ◈ Flask-powered backend
* ◈ Supabase PostgreSQL database
* ◈ Contact management system
* ◈ REST-style API endpoints
* ◈ Dashboard preview pages
* ◈ Admin contact interface
* ◈ Environment-variable based configuration
* ◈ Deployed and accessible through **Render**

---

## ✧ Live Experience

<div align="center">

### 🚀 Explore Synovixura

**[ OPEN LIVE WEBSITE → ](https://synovixura-website-flsk.onrender.com)**

<br/>

*Experience the interface instead of just reading about it.*

</div>

---

## ◈ Tech Stack

### Frontend

| Technology     | Purpose                                             |
| -------------- | --------------------------------------------------- |
| **HTML5**      | Semantic website structure                          |
| **CSS3**       | Layout, styling, responsive design & visual effects |
| **JavaScript** | Interactions, API communication & dynamic behaviour |
| **Jinja2**     | Flask-side HTML templating                          |

### Backend

| Technology     | Purpose                          |
| -------------- | -------------------------------- |
| **Python**     | Application backend              |
| **Flask**      | Web framework & routing          |
| **Supabase**   | Backend database platform        |
| **PostgreSQL** | Persistent contact data          |
| **REST API**   | Frontend ↔ backend communication |

### Deployment

| Platform     | Role                               |
| ------------ | ---------------------------------- |
| **Render**   | Production web hosting             |
| **GitHub**   | Source control & deployment source |
| **Supabase** | Cloud database                     |

---

## ◈ Architecture

```text
                         ┌──────────────────────┐
                         │      USER / WEB      │
                         └──────────┬───────────┘
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │   HTML / CSS / JS    │
                         │      FRONTEND        │
                         └──────────┬───────────┘
                                    │
                             HTTP / REST API
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │       FLASK          │
                         │       BACKEND        │
                         └──────────┬───────────┘
                                    │
                              Supabase API
                                    │
                                    ▼
                         ┌──────────────────────┐
                         │      SUPABASE        │
                         │    PostgreSQL DB     │
                         └──────────────────────┘
```

The application follows a simple full-stack flow:

**Browser → Frontend → Flask API → Supabase → Flask → Frontend**

This keeps the presentation layer separate from the backend logic and database layer.

---

## ◈ Core Features

### 01 — Immersive Landing Page

A modern landing page focused on visual hierarchy, typography, spacing and interactive sections.

### 02 — Bento-Style Layout

Content is organized using modular cards and sections inspired by modern Bento-style interfaces.

### 03 — Dark Aesthetic

The interface uses a dark visual system designed around contrast, minimalism and technology-focused aesthetics.

### 04 — Contact System

Visitors can submit:

```text
Name
Email
Company
Service
Message
Budget
```

Submissions are stored in the Supabase PostgreSQL database.

### 05 — Contact Management

The project includes an admin interface for viewing and managing submitted contacts.

Supported statuses:

```text
new
read
replied
archived
```

### 06 — REST API

The frontend communicates with Flask through dedicated API routes.

```text
GET     /api/health
GET     /api/contacts
GET     /api/contacts/<id>

POST    /api/contact

PATCH   /api/contacts/<id>

DELETE  /api/contacts/<id>
```

### 07 — Dashboard Previews

The project includes dedicated dashboard preview pages:

```text
/dashboard-1
/dashboard-2
```

These demonstrate the visual direction and product-oriented UI of the Synovixura ecosystem.

---

## ◈ Project Structure

```text
synovixura-flaskwebsite/
│
├── synovixura_flask/
│   ├── templates/
│   │   ├── ...
│   │
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── images/
│   │
│   └── ...
│
├── README.md
├── requirements.txt
├── app.py
├── .env.example
└── ...
```

> The exact structure may evolve as the project continues to grow.

---

## ◈ Run Locally

### Prerequisites

Make sure you have:

* **Python 3.x**
* **Git**
* A **Supabase** project

### 1. Clone the repository

```bash
git clone https://github.com/iamshubham27/synovixura-flaskwebsite.git

cd synovixura-flaskwebsite
```

### 2. Create a virtual environment

#### Windows

```bash
python -m venv venv

venv\Scripts\activate
```

#### macOS / Linux

```bash
python3 -m venv venv

source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file based on `.env.example`.

```env
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
SECRET_KEY=your_secret_key
```

**Never commit your real `.env` file or secret keys to GitHub.**

### 5. Start Flask

```bash
python app.py
```

The application should now be available at:

```text
http://127.0.0.1:5000
```

---

## ◈ Database

Synovixura uses **Supabase PostgreSQL** for persistent contact information.

The contact table contains fields such as:

```text
id
name
email
company
service
message
budget
status
ip_address
user_agent
created_at
updated_at
```

### Database flow

```text
Contact Form
     │
     ▼
POST /api/contact
     │
     ▼
Flask Backend
     │
     ▼
Supabase
     │
     ▼
PostgreSQL
```

---

## ◈ API Reference

### Health Check

```http
GET /api/health
```

Used to verify that the backend is running correctly.

---

### Get Contacts

```http
GET /api/contacts
```

Returns stored contact submissions.

---

### Get Single Contact

```http
GET /api/contacts/<id>
```

Returns a specific contact submission.

---

### Create Contact

```http
POST /api/contact
```

Example request:

```json
{
  "name": "John Doe",
  "email": "john@example.com",
  "company": "Example Inc.",
  "service": "Web Development",
  "message": "I would like to discuss a project.",
  "budget": "$5,000 - $10,000"
}
```

---

### Update Contact

```http
PATCH /api/contacts/<id>
```

Example:

```json
{
  "status": "replied"
}
```

Supported values:

```text
new
read
replied
archived
```

---

### Delete Contact

```http
DELETE /api/contacts/<id>
```

Removes the selected contact entry.

---

## ◈ Deployment

The application is deployed using **Render**.

### Deployment flow

```text
GitHub Repository
       │
       ▼
     Render
       │
       ▼
   Flask App
       │
       ▼
   Supabase
```

### Live deployment

**https://synovixura-website-flsk.onrender.com**

The project is configured to run as a Flask web application with its required environment variables supplied through the deployment environment.

---

## ◈ Security Note

This project is primarily intended as a **portfolio / demonstration project**.

If the contact-management API is exposed publicly, production deployment should include stronger access control around administrative operations.

Recommended improvements include:

* Authentication for `/admin`
* Authorization for contact-management APIs
* Restrictive Supabase Row Level Security policies
* Server-side validation
* Rate limiting
* CSRF protection where applicable
* Strong production secrets
* Protection against unauthorized `SELECT`, `UPDATE` and `DELETE` operations

**Do not expose private Supabase credentials in frontend code or commit them to GitHub.**

---

## ◈ Design Philosophy

Synovixura is built around a simple principle:

> ### **Technology should feel as good as it works.**

The interface intentionally combines:

```text
Minimalism
     +
Motion
     +
Typography
     +
Dark UI
     +
Information Density
     +
Functional Backend
```

The goal is not just to create another functional website, but to make the **engineering and visual experience feel like one product**.

---

## ◈ Roadmap

Potential future improvements:

* [ ] Secure admin authentication
* [ ] Advanced contact dashboard
* [ ] Better API authentication
* [ ] Improved database security policies
* [ ] Analytics dashboard
* [ ] More interactive page transitions
* [ ] Enhanced mobile experience
* [ ] Performance optimization
* [ ] SEO improvements
* [ ] Automated testing
* [ ] CI/CD pipeline
* [ ] Custom domain

---

## ◈ Contributing

Contributions, suggestions and improvements are welcome.

```bash
# Fork the repository

# Create a feature branch
git checkout -b feature/amazing-feature

# Commit your changes
git commit -m "Add amazing feature"

# Push the branch
git push origin feature/amazing-feature

# Open a Pull Request
```

---

## ◈ Author

<div align="center">

### **Shubham Biswas**

B.Tech Computer Science Engineering

**Government Engineering College, Jhalawar**

<br/>

<a href="https://github.com/iamshubham27">
  <img src="https://img.shields.io/badge/GitHub-iamshubham27-181717?style=for-the-badge&logo=github" alt="GitHub"/>
</a>

</div>

---

<div align="center">

### ✦ SYNOVIXURA

**Built with code. Designed with intent.**

<br/>

<a href="https://synovixura-website-flsk.onrender.com">
  <strong>Visit the Live Website →</strong>
</a>

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:111111,100:444444&height=120&section=footer" width="100%"/>

</div>
