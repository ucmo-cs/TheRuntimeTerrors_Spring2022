import json
import sys
from tkinter import CURRENT
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from common.dbconnector import mySQL_Connector
import common
from models.form import Form
from http import HTTPStatus

app = Flask(__name__)
api = Api(app)
db = mySQL_Connector()


class RiskForm(Resource):
    def post(self):
        risk_form = Form(request.get_json())
        
        riskJson = risk_form.data
        if db.check_record(risk_form.tripNumber):
            historicalSubQuery = f"Select activeSubmission from risk where tripNumber = \'{risk_form.tripNumber}\'"
            historical = db.select_record(historicalSubQuery)
            # print(historical[0][0], sys.stdout)
            updateRecordQuery = f"UPDATE risk SET lastUpdated = curdate(), totalRiskValue = \'17\',\
            activeSubmission = \'{json.dumps(riskJson)}\', historicalSubmission = \'{historical}\' WHERE tripNumber = \'{risk_form.tripNumber}\'"
            # print('*'*100)
            # print(updateRecordQuery, sys.stdout)
            # print('*'*100)
            db.insert_record(updateRecordQuery)
            return {'data': 'trip number already exists'}
        else:
            insertQuery = f'INSERT INTO risk(tripNumber, lastUpdated, totalRiskValue, activeSubmission) VALUES (\'{risk_form.tripNumber}\', curdate(), \'12\', \'{json.dumps(riskJson)}\')'
            db.insert_record(insertQuery)
        
        return risk_form.data, HTTPStatus.CREATED

    def get(self):
        return {'some json': 'test'}

    
api.add_resource(RiskForm, '/submit_risk_form')


if __name__ == "__main__":
    # app.run(debug=True, use_debugger=True)
    app.run()