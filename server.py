from flask import Flask
from flask_cors import CORS
from gmalthgtparser import HgtParser
import json
import math


app = Flask(__name__)
CORS(app)
@app.route('/')
def hello_world():
    return 'hello world'

@app.route('/elevation/<lat>/<lng>')
def elevation(lat, lng):
    print((float(lat), float(lng)))
    alt = get_elevation(lat, lng)
    print(alt)
    return str(alt[2])


def get_elevation(lat, lng):
    with HgtParser('N34E011.hgt') as parser:
        return parser.get_elevation((float(lat), float(lng)))