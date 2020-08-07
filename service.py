from flask import jsonify, json
from sklearn import preprocessing
import pickle
from sklearn import preprocessing
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
import math

inten_care = open("pickles/intensive_care_model.pkl","rb")
maternal = open("pickles/maternal_transfusion.pkl","rb")
perineal = open("pickles/perineal_laceration_model.pkl","rb")
ruptured = open("pickles/ruptured_uterus_model.pkl","rb")
transfusion = open("pickles/transfusion_model.pkl","rb")
unplanned = open("pickles/unplanned_hysterectomy_model.pkl","rb")

inten_care_model = pickle.load(inten_care)
maternal_model = pickle.load(maternal)
perineal_model = pickle.load(perineal)
ruptured_model = pickle.load(ruptured)
transfusion_model = pickle.load(transfusion)
unplanned_model = pickle.load(unplanned)

def predict(res):
    # race = res["input"][0]
    # num_of_visits = res["input"][1]
    # age = res["input"][2]
    race = 14   #white
    visits = 8  #7-8
    age = 3   #30-34
    
    values = pd.DataFrame([race, visits, age])
    values = values.reshape(-1, 1)
    percent = perineal_model.predict(values)
    print(percent)
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

    # return response
    return "Hit!"

