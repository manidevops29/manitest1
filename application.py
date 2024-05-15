from flask import Flask

app = Flask(__name__)

@app.route("/")
def welcom():
    return "<html><body><h1>Chandramani's App! Updated file</h1></body></html>"
