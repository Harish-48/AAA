import os
import requests
from flask import Flask, Response, request

app = Flask(__name__)
DESTINATION = os.environ.get("MAIN_URL")

@app.route('/<path:subpath>', methods=["GET", "POST"])
@app.route('/', methods=["GET", "POST"])
def proxy(subpath=""):
    url = f"{DESTINATION}/{subpath}"
    resp = requests.request(
        method=request.method,
        url=url,
        headers={key: value for key, value in request.headers if key != 'Host'},
        data=request.get_data(),
        cookies=request.cookies,
        allow_redirects=False
    )
    excluded_headers = ["content-encoding", "content-length", "transfer-encoding", "connection"]
    headers = [(name, value) for (name, value) in resp.raw.headers.items()
               if name.lower() not in excluded_headers]
    return Response(resp.content, resp.status_code, headers)

if __name__ == "__main__":
    app.run(port=5000, debug=True)
