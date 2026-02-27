from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>apply in a new city <select name=\"city\"><option>my new city</option></select></p><p>poster des photos/videos pour voir un job, langue que parler , sports, set yourself for a new life</p>"
