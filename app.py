from Modules.FlaskModule import *
from Modules.WebsocketModule import *
import time


BootError=False

class Application():
    def __init__(self):

        # Flaskı Başlat
        self.flask_module = FlaskModule(__name__)
        self.flask_module.run(BootError)

        # # Websocketi Başlat
        # self.websocket_module = WebsocketModule(self)
        # self.websocket_module.run()

Application()
while True:
    time.sleep(10)
    if BootError:
        print("BootError")
        time.sleep(10)
        break

# from flask import Flask

# app = Flask(__name__)


# @app.route("/")
# def index():
#     return "Hello, world!"
