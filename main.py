from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <html>
    <head>
        <title>Hello World</title>
    </head>
    <body>
        <h1>Hello</h1>
        <p>This is a sample fast app to demostrate CICD with jenkins, docker and kubernetes.</p>
    </body>
    </html>
    """
    return html_content

# Run the app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)