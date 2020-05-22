from methods.DatabaseMethods.ConnectToDB import connectToDataBase


def InsertPriceHistory(price, productId):
    query = f"insert into pricehistory (price, product_id) values ('{price}','{productId}')"

    connection = connectToDataBase()

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()

    cursor.close()
    connection.close()
