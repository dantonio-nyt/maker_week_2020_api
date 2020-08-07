import json
from flask import Flask
from flask_cors import CORS
from flask import request

import service
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/predict", methods = ['POST'])
def predict():
    response = request.json
    # get the json from the request
    # convert the json
    # pass obj into the function
    return service.predict(response)


if __name__ == "__main__":
    app.run()
