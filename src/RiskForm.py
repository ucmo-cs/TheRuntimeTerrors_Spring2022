import json
import re
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
        #     return risk_form.data, HTTPStatus.OK
        # else: 
        #     # create new record
        #     return risk_form.data, HTTPStatus.CREATED
        return risk_form.data

    def get(self):
        return {'test': 'test'}



    #     SQLquery = 'select activeSubmission from risk where id = ' + tripNumber
    

# @app.route("/results", methods = ['POST'])
# def submit_data():
#     sql = 'INSERT INTO risk(lastUpdated, totaRiskValue, activeSubmission) VALUES (%s, %s, %s)'
api.add_resource(RiskForm, '/submit_risk_form')


if __name__ == "__main__":
    app.run(debug=True) 