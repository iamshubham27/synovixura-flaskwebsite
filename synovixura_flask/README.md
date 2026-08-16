# Synovixura Tech — Flask + Supabase

Same design, copy, and interactions as the original Synovixura-Website
repo (Bento Grid layout, dark mode, dashboard previews) — HTML/CSS/JS
ported as-is. Backend is Flask, data lives in your **Supabase**
Postgres project (`Synovixura`, table `contacts`) instead of
Node/Express + Supabase JS or SQLite.

## 1. Local setup

```bash
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp .env.example .env
```

Edit `.env`:

```
SUPABASE_URL=https://iqxsbgfudnhyosiclvfm.supabase.co
SUPABASE_KEY=<your anon/publishable key — Supabase dashboard → Settings → API>
SECRET_KEY=<any random string>
```

Then:

```bash
python app.py
```

Visit http://127.0.0.1:5000

## About the database

The `contacts` table already exists in your Supabase project with
this schema:

```
id, name, email, company, service, message, budget,
status (default 'new'), ip_address, user_agent,
created_at, updated_at
```

**Row Level Security is enabled with fully open policies** (public
insert/select/update/delete) — this matches how the original repo's
Supabase table was configured, since the site had no admin login
either. That means anyone with your anon key can read, edit, or
delete every contact submission. Fine for a demo/personal project;
before using this for a real client-facing form, you'll want to:

- Add a real login to `/admin` (Flask-Login + a users table, or
  HTTP basic auth at minimum), **and**
- Tighten the RLS policies so `SELECT`/`UPDATE`/`DELETE` require an
  authenticated/service role, keeping `INSERT` open for the public
  contact form.

Ask me if you'd like help with either of those — happy to wire up a
simple password gate and updated RLS policies.

## 2. Deploying on PythonAnywhere

1. **Create a PythonAnywhere account** (the free tier works for this).
2. **Upload the project.** Easiest path: push this project to a
   GitHub repo, then in a PythonAnywhere **Bash console**:
   ```bash
   git clone <your-repo-url> synovixura
   cd synovixura
   ```
   (Or use the Files tab to upload the zip and unzip it there.)
3. **Create a virtualenv** (in the same Bash console):
   ```bash
   mkvirtualenv --python=/usr/bin/python3.10 synovixura-venv
   pip install -r requirements.txt
   ```
4. **Create a new Web App:**
   - Go to the **Web** tab → **Add a new web app**
   - Choose **Manual configuration** (not the Flask wizard) → your
     Python version
   - Set **Source code** to the project folder path (e.g.
     `/home/yourusername/synovixura`)
   - Set **Virtualenv** to the path from step 3 (e.g.
     `/home/yourusername/.virtualenvs/synovixura-venv`)
5. **Edit the WSGI config file** (link is on the Web tab, something
   like `/var/www/yourusername_pythonanywhere_com_wsgi.py`). Replace
   its contents with:
   ```python
   import sys
   import os

   project_home = '/home/yourusername/synovixura'
   if project_home not in sys.path:
       sys.path.insert(0, project_home)

   # Environment variables — free tier has no env-vars UI, so set
   # them here directly (paid tiers can use the Web tab's env vars
   # section instead and skip this block).
   os.environ['SUPABASE_URL'] = 'https://iqxsbgfudnhyosiclvfm.supabase.co'
   os.environ['SUPABASE_KEY'] = 'your-anon-key-here'
   os.environ['SECRET_KEY'] = 'something-random'

   from app import app as application
   ```
6. **Set the static files mapping** (Web tab → Static files):
   - URL: `/static/`
   - Directory: `/home/yourusername/synovixura/static`
7. Hit the green **Reload** button on the Web tab, then visit
   `https://yourusername.pythonanywhere.com`.

PythonAnywhere's free tier allows outbound HTTPS to Supabase, so the
`/api/contact` and `/api/contacts` routes will work as-is.

## Pages

- `/` — home
- `/contact` — contact form
- `/dashboard-1`, `/dashboard-2` — static dashboard previews
- `/admin` — contact submissions list (no login — see security note above)

## API (unchanged contract, now backed by Supabase)

- `GET /api/health`
- `GET /api/contacts`
- `GET /api/contacts/<id>`
- `POST /api/contact` — `{name, email, company, service, message, budget}`
- `PATCH /api/contacts/<id>` — `{status}` (`new|read|replied|archived`)
- `DELETE /api/contacts/<id>`

The front-end JS in `contact.html` and `admin.html` is untouched — it
already talks to these exact routes.
