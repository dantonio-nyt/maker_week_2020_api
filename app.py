from flask import Flask
from flask_cors import CORS

import service
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/predict")
def predict():
    return service.predict()


if __name__ == "__main__":
    app.run()
