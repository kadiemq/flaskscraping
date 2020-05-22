from methods.DatabaseMethods.ConnectToDB import connectToDataBase
from methods.DatabaseMethods.InsertPriceHistory import InsertPriceHistory


def InsertDB(check_for, data):
    if check_for == 'product':
        query = f"insert into product (title, country, ASIN, current_price, price_string, image_url, product_url) " \
                f"values ('{data.title}', '{data.country}', '{data.asin}', '{data.price}'," \
                f" '{data.price_string}', '{data.image_url}', '{data.url}') returning id"
    else:
        query = f"insert into user_table (email, first_name, last_name, password) " \
                f"VALUES ('{data.email}', '{data.first_name}', '{data.last_name}', '{data.password}') returning id"

    connection = connectToDataBase()

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    resultId = result[0]['id']
    if check_for == 'product':
        InsertPriceHistory(data.price, resultId)

    return resultId
