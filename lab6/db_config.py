import mysql.connector

def connect():
    return mysql.connector.connect(
        host='localhost',
        user='root',
        password='B!gM!k26',
        database='guitar_shop'
    )
