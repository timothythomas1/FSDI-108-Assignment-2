from flask import Flask
from data import me

import json

app = Flask(__name__)

@app.get("/")
def home():
    return "Hello from flask"

@app.get("/test")
def test():
    return "This is just another endpoint"

@app.get("/about")
def about():
    return "Tim Thomas"


###########################################################################################
################################ API PRODUCTS #############################################
###########################################################################################

@app.get("/api/test")
def test_api():
    return json.dumps("OK")

@app.get("/api/about")
def about_api():
    return json.dumps(me)

app.run(debug=True)
