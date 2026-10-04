from urllib import request

from fastapi import FastAPI
import uvicorn
from starlette.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/")
def index():
    return templates.TemplateResponse({"request": request}, "index.html")


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)

