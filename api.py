#from fastapi import FastAPI, Request
#from fastapi.responses import HTMLResponse
#from fastapi.templating import Jinja2Templates

from microdot import Microdot
from jinja2 import Environment, FileSystemLoader

from controller import Controller


app = Microdot()

# Opsæt Jinja2
env = Environment(loader=FileSystemLoader('templates'))
#app = FastAPI()
#templates = Jinja2Templates(directory="templates")
controller = Controller()

def render_status(status):
    template = env.get_template('status.html')
    html = template.render(status)
    return html, 200, {'Content-Type': 'text/html'}

@app.get("/drive/forward")
def drive(request: Request):
    controller.forward()
    status = controller.status()
    return render_status(status)
#    status["request"] = request
#    return templates.TemplateResponse("status.html", status)


@app.get("/drive/reverse")
def reverse(request: Request):
    controller.reverse()
    status = controller.status()
    return render_status(status)
#    status["request"] = request
#    return templates.TemplateResponse("status.html", status)


@app.get("/stop")
def drive(request: Request):
    controller.stop()
    status = controller.status()
    return render_status(status)
#    status["request"] = request
#    return templates.TemplateResponse("status.html", status)


@app.get("/turn/left")
def turn_left(request: Request):
    controller.left()
    status = controller.status()
    return render_status(status)
#    status["request"] = request
#    return templates.TemplateResponse("status.html", status)


@app.get("/turn/right")
def turn_right(request: Request):
    controller.right()
    status = controller.status()
    return render_status(status)
#    status["request"] = request
#    return templates.TemplateResponse("status.html", status)


@app.get("/turn/straight")
def turn_straight(request: Request):
    controller.straight()
    status = controller.status()
    return render_status(status)
#    status["request"] = request
#    return templates.TemplateResponse("status.html", status)


@app.get("/") #, response_class=HTMLResponse)
def home(request: Request):
    template = env.get_template('home.html')
    html = template.render(name="Pi Zero")
    return html, 200, {'Content-Type': 'text/html'}
#    return templates.TemplateResponse("home.html", {"request": request})

app.run(host="0.0.0.0", port=8080, debug=True)
