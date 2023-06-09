from Modules.FlaskModule import *
from Modules.WebsocketModule import *
import time


BootError=False

class Application():
    def __init__(self):
        # Mongodb'ye bağlan
        self.database = DatabaseModule()
        self.database.connect_db()

        # Flaskı Başlat
        self.flask_module = FlaskModule(__name__,self)
        self.flask_module.run(BootError)

        # Websocketi Başlat
        self.websocket_module = WebsocketModule(self)
        self.websocket_module.run()



Application()
while True:
    time.sleep(10)
    if BootError:
        print("BootError")
        time.sleep(10)
        break

# from flask import Flask
# from flask import render_template

# app = Flask(__name__)

# @app.route("/")
# def index():
#     return render_template('home.html')


# app.run()


