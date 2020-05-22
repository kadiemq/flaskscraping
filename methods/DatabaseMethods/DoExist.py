from methods.DatabaseMethods.ConnectToDB import connectToDataBase


def DoExist(check_for, data):

    if check_for == 'product':
        query = f"select exists(select * from product where asin = '{data.asin}' and country = '{data.country}')"
    else:
        query = f"select exists(select * from user_table where email = '{data}')"

    connection = connectToDataBase()

    cursor = connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    cursor.close()
    connection.close()

    doExists = result[0]['exists']

    if doExists:
        return True
    else:
        return False
