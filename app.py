import os
import random
import string
from flask import Flask, redirect, request, render_template_string

app = Flask(__name__)

# Destination site to redirect to (fallback is your notes site)
MAIN_URL = os.environ.get("MAIN_URL", "https://harish-python-notes.vercel.app")

def random_slug(n: int = 6) -> str:
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=n))

INDEX_TEMPLATE = """
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Dynamic Redirect Link</title>
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; 
           max-width: 720px; margin: 56px auto; padding: 0 16px; line-height: 1.5; }
    h1 { font-size: 28px; margin-bottom: 12px; }
    .box { background: #f4f4f4; padding: 12px 14px; border-radius: 10px; }
    .link { font-size: 18px; word-break: break-all; }
    .muted { color: #444; }
    button { padding: 8px 12px; border-radius: 8px; border: 1px solid #ccc; cursor: pointer; }
    a.btn { display: inline-block; margin-top: 12px; }
  </style>
</head>
<body>
  <h1>Dynamic Redirect Link</h1>
  <p class="muted">
    Share this link (it always redirects to <code>{{ main_url }}</code>):
  </p>
  <div class="box">
    <p class="link"><a href="{{ random_link }}">{{ random_link }}</a></p>
    <p>
      <button onclick="navigator.clipboard.writeText('{{ random_link }}')">Copy link</button>
      <a class="btn" href="/" onclick="return true;">Generate another</a>
    </p>
  </div>
  <p class="muted">Any path on this domain (e.g. <code>/abc123</code>) will 302-redirect to your destination.</p>
</body>
</html>
"""

@app.route("/")
def home():
    slug = random_slug()
    # request.host_url includes trailing slash – normalize then append slug
    base = request.host_url.rstrip('/')
    link = f"{base}/{slug}"
    return render_template_string(INDEX_TEMPLATE, random_link=link, main_url=MAIN_URL)

@app.route("/healthz")
def health():
    return "ok", 200

@app.route("/<path:subpath>")
def dynamic_redirect(subpath: str):
    # Optional: log/inspect subpath if needed
    return redirect(MAIN_URL, code=302)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port)