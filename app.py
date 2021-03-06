from flask import Flask, jsonify # <-- sends dictionary back
from flask_cors import CORS
import random

app = Flask(__name__)
CORS(app)

affirms = ["You are loved",
           "Keep going ^-^",
           "You are precious",
           "Believe in yourself! ⧹(⦁ᴗ⦁)⧸",
           "Your experiences are valid <3",
           "!!! You Got this !!!",
           "Life is valuable, and you are too!"
           "You look like a snack （＾ω＾）"]

randomaffirm = random.choice(affirms)

@app.route('/')
def index():
    return jsonify({"content": randomaffirm})