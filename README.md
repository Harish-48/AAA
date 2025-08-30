# Dynamic Redirector (Flask)

A tiny Flask app that generates **random URLs** like `/Ab3xPq` which **302-redirect** to a single destination (your main site).

Default destination is `https://harish-python-notes.vercel.app`, configurable via the `MAIN_URL` environment variable.

---

## Run locally

```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
# source .venv/bin/activate

pip install -r requirements.txt
# set destination (optional)
# Windows (Powershell):  $env:MAIN_URL="https://example.com"
# macOS/Linux (bash):    export MAIN_URL="https://example.com"

python app.py
# open http://127.0.0.1:5000
```

## Deploy on Render (recommended for Flask)

1. Push this folder to a **GitHub repo**.
2. Create a free account at **https://render.com**.
3. Click **New → Web Service**, connect your repo.
4. **Environment**: `Python`
5. **Build Command**: `pip install -r requirements.txt`
6. **Start Command**: `gunicorn app:app`
7. Add an environment variable: `MAIN_URL=https://harish-python-notes.vercel.app` (or your desired URL).
8. Deploy. Your app will get a domain like `https://dynamic-redirector.onrender.com`.

- Open the base URL to get a **fresh random link** to share.
- Visiting any path (`/abc123`, `/hello`, `/foo/bar`) will redirect to the `MAIN_URL` with HTTP 302.

## Notes

- This app **does not** store slugs; it simply redirects **any** path to the destination. If you need per-slug destinations, add a DB (Redis or SQL) to map slugs → URLs.
- To enforce HTTPS everywhere, make sure your platform adds TLS (Render does).
- If you want a custom domain, you can add it in your hosting provider and point DNS accordingly.