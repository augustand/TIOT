# encoding=utf-8
from flask import render_template

from app import app

# user = Blueprint('tw', __name__, template_folder='/tw')  # 蓝图可以动态的定义模板文件的位置

@app.route('/')
@app.route('/index')
def index():
    return render_template("/hello.html")

@app.route('/client')
def client():
    return render_template("/client.html")


@app.route('/lht')
def light():
    return render_template("/light.html")


@app.route('/rfid_client')
def rfid():
    return render_template("/rfid_client.html")