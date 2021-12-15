# 彭彭youtube教學 lesson 9 以後
# https://www.youtube.com/watch?v=7NWmRmMOgz8

from flask import Flask, app
from flask import request 
from flask import render_template

#建立Application物件，設定靜態檔案的路徑處理
app = Flask(__name__, static_folder="public", static_url_path="/")

#處理路徑 / 的對應函式

@app.route("/")
def index():
    return render_template("index.html")

#處理路徑
app.run()



