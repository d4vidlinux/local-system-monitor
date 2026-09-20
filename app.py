from flask import Flask, render_template
from system_functions import *

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template(
        "index.html"
    )

@app.route("/api/resources")
def temperature():
    return {
        "cpu": cpu(),
        "motherboard": motherboard(),
        "gpu": gpu(),
        "uptime": uptime()
    }

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)