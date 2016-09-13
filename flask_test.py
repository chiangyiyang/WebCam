#!/urs/bin/python
# -*- coding:UTF-8 -*-

from flask import Flask, url_for
from yytools.camera import getImage
from yytools.led import blink

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/get_img")
def get_img():
    imgfile = getImage()
    blink(1)
    # return "Got an image!<br>" + imgfile
    # return app.send_static_file('1473752822.31.jpg')
    return '<img src="' + url_for('static',
                                  filename=imgfile) + '" alt="Image View" style="width:304px;height:228px;">' \
           + '<input type="button" onClick="window.location.reload()" value="Capture">'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
