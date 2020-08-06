from flask import jsonify, json


def predict():

    # trained models logic goes here...

    # get all of our predictions

    # arrange into a dictionary
    # 6 different issues
    dictionary = {
        "Maternal Transfusion": 0.30,
        "Pernieal Laceration": 0.40,
        "Ruptured Uterus": 0,
        "Unplanned Hysterectomy": 0,
        "Intensive Care": 0.30
    }
    response = jsonify(
        response=json.dumps(dictionary),
        status=200,
        mimetype='application/json'
    )

    # handle some errors
    # if True:
    #     response = jsonify(
    #         response=json.dumps("something went wrong"),
    #         status=500,
    #         mimetype='application/json'
    #     )

    return response

