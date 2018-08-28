from flask import Flask, render_template
import socket
import random
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return(socket.gethostname())

if __name__ == "__main__":
    app.run(host="0.0.0.0")