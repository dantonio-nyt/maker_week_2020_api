from flask import Flask
import service
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/api/predict")
def predict():
    return service.predict()


if __name__ == "__main__":
    app.run()