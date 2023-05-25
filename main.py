import flask
import pandas as pd
import json


app = flask.Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    well = flask.request.args.get('well')

    file_data = pd.read_excel('newfile.xls')
    json_data = file_data.to_json()
    dict_data = json.loads(json_data)

    indexOfAPI =[]
    oil_total = 0
    gas_total = 0
    brine_total = 0

    for i in dict_data["API WELL  NUMBER"]:
        if dict_data["API WELL  NUMBER"][i] == int(well):
            indexOfAPI.append(i)
    for i in indexOfAPI:
        if dict_data["QUARTER 1,2,3,4"][i]:
            oil_total = oil_total + dict_data["OIL"][i]


    for i in dict_data["API WELL  NUMBER"]:
        if dict_data["API WELL  NUMBER"][i] == int(well):
            indexOfAPI.append(i)
    for i in indexOfAPI:
        if dict_data["QUARTER 1,2,3,4"][i]:
            gas_total = gas_total + dict_data["GAS"][i]

            
    for i in dict_data["API WELL  NUMBER"]:
        if dict_data["API WELL  NUMBER"][i] == int(well):
            indexOfAPI.append(i)
    for i in indexOfAPI:
        if dict_data["QUARTER 1,2,3,4"][i]:
            brine_total = brine_total + dict_data["BRINE"][i]

    return flask.jsonify({"oil":oil_total},
                         {"gas":gas_total},
                         {"brine",brine_total})

if __name__ == '_main_':
       app.run(debug=True, port=3000)