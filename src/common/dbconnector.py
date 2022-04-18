from dis import dis
from flask import jsonify
from mysql.connector import connect, Error
import mysql.connector
import sys


class mySQL_Connector:
    def __init__(self):
        try:
            self.cnx = mysql.connector.connect(
                host='localhost',
                user='root',
                password='Ryker723$',
                database='flight_risk'
            )
            self.cursor = self.cnx.cursor(buffered = True)
        except mysql.connector.Error as err:
            if err.errno == mysql.connector.errorcode.ER_ACCESS_DENIED_ERROR:
                print('something is wrong with your username or password')
            elif err.errno == mysql.errorcode.ER_BAD_DV_ERROR:
                print("Database does not exist")
            else:
                print(err)
                exit()
    
    def insert_record(self, query):
        self.cursor.execute(query)
        self.cnx.commit()


    def check_record(self, tripNumber):
        query = f"Select tripNumber from risk where tripNumber = \'{tripNumber}\' LIMIT 1"
        self.cursor.execute(query)
        tripCount = self.cursor.fetchall()
        print(tripCount, file=sys.stdout)
        if tripCount:
            print('yay', file=sys.stdout)
            return True
        else:
            print('error', file=sys.stdout)
            return False

    
    def select_record(self, query):
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        result = result[0][0]
        return result
         

    def close_connection(self):
        self.cnx.close()
        