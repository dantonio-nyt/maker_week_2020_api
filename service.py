from flask import jsonify, json


def predict():

    # trained model logic goes here...

    prediction = [[0.66, 0.33]]
    response = jsonify(
        response=json.dumps(prediction),
        status=200,
        mimetype='application/json'
    )
    return response
