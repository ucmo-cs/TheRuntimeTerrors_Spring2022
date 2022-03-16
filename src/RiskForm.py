import json
import re
from tkinter import CURRENT
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from common.dbconnector import mySQL_Connector
from models.form import Form
from http import HTTPStatus

app = Flask(__name__)
api = Api(app)
db = mySQL_Connector()
 

# def main_page():
#     query = 'select flightInformation from risk'
#     info = db.get_all_db(query)
#     return("HI")


class RiskForm(Resource):
    def post(self):
        print(request)
        risk_form = Form(request.get_json())
        # if db.check_record(risk_form.tripNumber):
        #     # check for changed fields
        #     # do an update with changed fields
        #     historicalSubQuery = f"Select activeSubmission from risk where tripNumber = {risk_form.tripNumber}"
        #     historicalSub = db.get_all_db(historicalSubQuery) 
        #     updateRecordQuery = f"UPDATE risk SET lastUpdated = CURRENTDATE, totalRiskValue = '12',\
        #     activeSubmission = {risk_form.data}, historicalSubmission = {historicalSub} WHERE tripNumber = {risk_form.tripNumber}"
        #     updateRecord = db.get_all_db(updateRecordQuery)
        #     return risk_form.data, HTTPStatus.OK
        # else: 
        #     # create new record CHANGE TRIP RISK VAL
        riskJson = risk_form.data
        insertQuery = f'INSERT INTO risk(tripNumber, lastUpdated, totalRiskValue, activeSubmission) VALUES (\'{risk_form.tripNumber}\', curdate(), \'12\', \'{json.dumps(riskJson)}\')'

        db.get_all_db(insertQuery)

            # return risk_form.data, HTTPStatus.CREATED
        return riskJson

    def get(self):
        return {'test': 'test'}

    

# @app.route("/results", methods = ['POST'])
# def submit_data():
#     sql = 'INSERT INTO risk(lastUpdated, totaRiskValue, activeSubmission) VALUES (%s, %s, %s)'
api.add_resource(RiskForm, '/submit_risk_form')


if __name__ == "__main__":
    app.run(debug=True) 