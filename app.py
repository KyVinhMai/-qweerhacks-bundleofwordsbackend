from flask import Flask
from flask import Flask
from flask_cors import CORS

app = Flask(name)
CORS(app)

app = Flask(__name__)

@app.route('/')
def index():
    return "What's jiggy!"