from flask import jsonify, json


def predict():

    # trained model logic goes here...
    # 6 different issues
    prediction = [[0.66, 0.33, 0, 0 , 0]]
    # retValue = {
    #
    # }
    response = jsonify(
        response=json.dumps(prediction),
        status=200,
        mimetype='application/json'
    )
    return response

