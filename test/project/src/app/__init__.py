# encoding=utf-8
from flask import Flask

app = Flask(__name__)
app.debug = True
app.host = '0.0.0.0'
app.config.from_object('app.common.setting')
#这句话的意思就是导入controller模块,不导入程序就会出现找不到路径问题
from app.controller import controller

