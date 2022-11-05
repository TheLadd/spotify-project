from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def default():
   return "Return a json here?"