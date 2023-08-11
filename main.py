"""
This module defines a FastAPI app that serves a simple HTML page.
"""

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    """
    Return an HTML response for the root endpoint.
    """
    html_content = """
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello</h1>
        <p>This is a sample fast app to demonstrate CICD with Jenkins, Docker, and Kubernetes.</p>
    </body>
    </html>
    """
    return html_content

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)
