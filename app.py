import os
import mysql.connector
import datetime
import json
from flask import Flask, request, make_response, send_file

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev'
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="riskAssessmentTool"
    )

    # Create New Risk Assessment Entry in Database Based Off JSON Object
    @app.route('/riskassessments/create', methods=['POST'])
    def add_risk_assessment_by_json():
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            data = request.json
            dbcursor = database.cursor()
            sql = "INSERT INTO RiskAssessments (TripNumber, LastUpdated, FlightInformation, ActiveSubmission) VALUES (%s, %s, %s, %s)"
            values = (data['FlightInformation']['Release/Trip #'], datetime.datetime.now(), json.dumps(data['FlightInformation']), json.dumps(list(data.values())))
            dbcursor.execute(sql, values)
            database.commit()
            return data
        else:
            return 'Content-Type not supported!'

    # Create New Blank Risk Assessment Entry in Database Based Off Passed In ID
    @app.route('/riskassessments/create/<id>', methods=['POST'])
    def add_blank_risk_assessment_by_id(id):
        dbcursor = database.cursor()
        sql = "INSERT INTO RiskAssessments (TripNumber, LastUpdated) VALUES (%s, %s)"
        values = (id, datetime.datetime.now())
        dbcursor.execute(sql, values)
        database.commit()
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}

    # Update Risk Assessment Entry in Database Based Off JSON Object
    # @app.route('/riskassessments/update', methods=['POST'])
    # def update_risk_assessment_by_json():
    #     content_type = request.headers.get('Content-Type')
    #     if (content_type == 'application/json'):
    #         data = request.json
    #         dbcursor = database.cursor()
    #         sql = "INSERT INTO RiskAssessments (TripNumber, LastUpdated, FlightInformation, ActiveSubmission) VALUES (%s, %s, %s, %s)"
    #         values = (data['FlightInformation']['Release/Trip #'], datetime.datetime.now(), json.dumps(data['FlightInformation']), json.dumps(data))
    #         dbcursor.execute(sql, values)
    #         database.commit()
    #         return data
    #     else:
    #         return 'Content-Type not supported!'

    # Send BlankFlight.json File
    @app.route('/riskassessments', methods=['GET'])
    def get_blank_risk_assessment():
        return make_response(send_file("BlankFlight.json"))

    # Delete Risk Assessment Entry in Database Based Off JSON Object
    @app.route('/riskassessments/delete/<id>', methods=['DELETE'])
    def delete_risk_assessment_by_id(id):
        dbcursor = database.cursor()
        sql = "DELETE FROM RiskAssessments WHERE TripNumber=" + id
        dbcursor.execute(sql)
        database.commit()
        return make_response("", 204)

    return app