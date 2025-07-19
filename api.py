from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from controller import Controller

app = FastAPI()
templates = Jinja2Templates(directory="templates")
controller = Controller()

@app.get("/drive/forward")
def drive(request: Request):
    controller.forward()
    status = controller.status()
    status["request"] = request
    return templates.TemplateResponse("status.html", status)


@app.get("/drive/reverse")
def reverse(request: Request):
    controller.reverse()
    status = controller.status()
    status["request"] = request
    return templates.TemplateResponse("status.html", status)


@app.get("/stop")
def drive(request: Request):
    controller.stop()
    status = controller.status()
    status["request"] = request
    return templates.TemplateResponse("status.html", status)


@app.get("/turn/left")
def turn_left(request: Request):
    controller.left()
    status = controller.status()
    status["request"] = request
    return templates.TemplateResponse("status.html", status)


@app.get("/turn/right")
def turn_right(request: Request):
    controller.right()
    status = controller.status()
    status["request"] = request
    return templates.TemplateResponse("status.html", status)


@app.get("/turn/straight")
def turn_straight(request: Request):
    controller.straight()
    status = controller.status()
    status["request"] = request
    return templates.TemplateResponse("status.html", status)


@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})
