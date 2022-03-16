from dis import dis
from flask import jsonify
from mysql.connector import connect, Error
import mysql.connector


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
    
    def get_all_db(self, query):
        self.cursor.execute(query)
        #display_info = self.cursor.fetchall()
        self.cnx.commit()
        self.cnx.close()
        #return display_info


    def check_record(self, tripNumber):
        query = f"Select count(*) from risk where tripNumber = {tripNumber}"
        self.cursor.execute(query)
        tripCount = self.cursor.fetchone()
        if(tripCount != '0'):
            self.cnx.commit()
            self.cnx.close()
            return True
        else:
            self.cnx.commit()
            self.cnx.close()
            return False
        

        
        