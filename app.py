import os
import mysql.connector
import datetime
import json
from flask import Flask, request, make_response, send_file

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
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

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="riskAssessmentTool"
    )

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    @app.route('/riskassessments', methods=['POST'])
    def process_json():
        content_type = request.headers.get('Content-Type')
        if (content_type == 'application/json'):
            json2 = request.json
            # print(json)
            mycursor = mydb.cursor()
            sql = "INSERT INTO RiskAssessments (TripNumber, LastUpdated, FlightInformation) VALUES (%s, %s, %s)"
            val = ("1006", datetime.datetime.now(), json.dumps(json2))
            mycursor.execute(sql, val)
            mydb.commit()
            print(mycursor.rowcount, "record inserted.")
            return json2
        else:
            return 'Content-Type not supported!'

    @app.route('/riskassessments', methods=['GET'])
    def get_blank_risk_assessment():
        return make_response(send_file("BlankFlight.json"))

    @app.route('/riskassessments/delete/<id>', methods=['DELETE'])
    def delete_risk_assessment_by_id(id):
        mycursor = mydb.cursor()
        sql = "DELETE FROM RiskAssessments WHERE TripNumber=" + id
        mycursor.execute(sql)
        mydb.commit()
        return make_response("", 204)

    return app