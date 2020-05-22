from methods.DatabaseMethods.ConnectToDB import connectToDataBase
from methods.DatabaseMethods.InsertPriceHistory import InsertPriceHistory


def UpdateProduct(product):
    query = f"update product set current_price = '{product.price}' where asin = '{product.asin}' and country = '{product.country}' returning id"

    price = GetDatabaseProduct(product)
    if price != product.price:
        priceChanged = True
    else:
        priceChanged = False

    connection = connectToDataBase()

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    productId = result[0]['id']
    InsertPriceHistory(product.price, productId)
    return {productId, priceChanged}


def GetDatabaseProduct(product):
    query = f"select current_price from product where asin = '{product.asin}' and country = '{product.country}'"

    connection = connectToDataBase()

    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    price = result[0]['current_price']
    return price
