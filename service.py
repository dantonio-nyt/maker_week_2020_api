from flask import jsonify, json
from sklearn import preprocessing
import pickle
from sklearn import preprocessing
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import math

inten_care = open("pickles/intensive_care_model.pkl","rb")
perineal = open("pickles/perineal_laceration_model.pkl","rb")
ruptured = open("pickles/ruptured_uterus_model.pkl","rb")
transfusion = open("pickles/transfusion_model.pkl","rb")
unplanned = open("pickles/unplanned_hysterectomy_model.pkl","rb")

inten_care_model = pickle.load(inten_care)
perineal_model = pickle.load(perineal)
ruptured_model = pickle.load(ruptured)
transfusion_model = pickle.load(transfusion)
unplanned_model = pickle.load(unplanned)

def predict(req):
    race = req["input"][0]
    num_of_visits = req["input"][1]
    age = req["input"][2]
    # race = 14   #white
    # visits = 8  #7-8
    # age = 3   #30-34
    
    values = pd.DataFrame([[race, num_of_visits, age]])
    pernieal_percent = perineal_model.predict_proba(values)
    ruptured_percent = ruptured_model.predict_proba(values)
    tranfusion_percent = transfusion_model.predict_proba(values)
    unplanned_percent = unplanned_model.predict_proba(values)
    inten_care_percent = inten_care_model.predict_proba(values)

    no_complication = (1 - pernieal_percent[0][1] + pernieal_percent[0][2]) * (1 - ruptured_percent[0][1] + ruptured_percent[0][2]) * (1 - tranfusion_percent[0][1] + tranfusion_percent[0][2]) * (1 - unplanned_percent[0][1] + unplanned_percent[0][2]) * (1 - inten_care_percent[0][1] + inten_care_percent[0][2])
    # trained models logic goes here...

    # get all of our predictions

    # arrange into a dictionary
    # 6 different issues
    dictionary = {
        "Maternal Transfusion": tranfusion_percent[0][1] + tranfusion_percent[0][2],
        "Pernieal Laceration": pernieal_percent[0][1] + pernieal_percent[0][2],
        "Ruptured Uterus": ruptured_percent[0][1] + ruptured_percent[0][2],
        "Unplanned Hysterectomy": unplanned_percent[0][1] + unplanned_percent[0][2],
        "Intensive Care": inten_care_percent[0][1] + inten_care_percent[0][2],
        "no_complication": no_complication
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

    # return response
    return response

