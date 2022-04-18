import json
import sys
from tkinter import CURRENT
from flask import Flask, Response, make_response, render_template, request, jsonify, send_file
from flask_restful import Resource, Api
from common.dbconnector import mySQL_Connector
from common.create_html import MakeJson
from models.form import Form
from http import HTTPStatus


app = Flask(__name__)
api = Api(app)
db = mySQL_Connector()
mkjson = MakeJson()

class RiskForm(Resource):
    def post(self):
        print(request)
        risk_form = Form(request.get_json())
        
        riskJson = risk_form.data
        flightInfo = risk_form.flightData
        if db.check_record(risk_form.tripNumber):
            historicalSubQuery = f"Select activeSubmission from risk where tripNumber = \'{risk_form.tripNumber}\'"
            historical = db.select_record(historicalSubQuery)
            updateRecordQuery = f"UPDATE risk SET lastUpdated = curdate(), totalRiskValue = \'{risk_form.totalRiskValue}\',\
            activeSubmission = \'{json.dumps(riskJson)}\', historicalSubmission = \'{historical}\' WHERE tripNumber = \'{risk_form.tripNumber}\'"
            db.insert_record(updateRecordQuery)
            #return risk_form.totalRiskValue
        else:
            insertQuery = f'INSERT INTO risk(tripNumber, lastUpdated, flightInformation, totalRiskValue, activeSubmission) VALUES (\'{risk_form.tripNumber}\', curdate(), \'{json.dumps(flightInfo)}\', \'{risk_form.totalRiskValue}\', \'{json.dumps(riskJson)}\')'
            db.insert_record(insertQuery)
        myjson = jsonify({"risk value": risk_form.totalRiskValue})
        headers = {'Content-Type': 'text/html'} 
        return make_response(myjson, 201, headers)
        # return risk_form.totalRiskValue, HTTPStatus.CREATED
    
    def delete(self):
        pass

class ReturnHTML(Resource):
    def get(self):
        mkjson.make_json()
        headers = {'Content-Type': 'text/html'} 
        return make_response(send_file('models/index.html'),200,headers)
    
api.add_resource(RiskForm, '/submit_risk_form')
api.add_resource(ReturnHTML, '/')


if __name__ == "__main__":
    app.run(debug=True)
    # app.run()