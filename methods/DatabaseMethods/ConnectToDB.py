import psycopg2
from flask import jsonify
from psycopg2.extras import RealDictCursor

from Constants import getAllProductsQuery


def connectToDataBase():
    connection = psycopg2.connect(user="postgres",
                                  password="",
                                  host="localhost",
                                  port="5432",
                                  database="",
                                  cursor_factory=RealDictCursor)
    return connection

# def get_asin():
#     connection = connectToDataBase()
#
#     cursor = connection.cursor()
#
#     cursor.execute(getAllProductsQuery)
#     products = cursor.fetchall()
#
#     cursor.close()
#     connection.close()
#
#     Asin = products[0]['asin']
#     return Asin
#
#
# def get_title():
#     connection = connectToDataBase()
#
#     cursor = connection.cursor()
#
#     cursor.execute(getAllProductsQuery)
#     products = cursor.fetchall()
#
#     cursor.close()
#     connection.close()
#
#     response = jsonify(products)
#     Title = products[0]['title']
#     return Title
