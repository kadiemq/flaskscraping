from methods.DatabaseMethods.ConnectToDB import connectToDataBase


def GetOneDB(check_for, attr, value):
    if check_for == 'product':
        query = f"select * from product where {attr} = '{value}'"
    else:
        query = f"select * from user_table where {attr} = '{value}'"

    connection = connectToDataBase()

    cursor = connection.cursor()
    cursor.execute(query)
    connection.commit()
    fetchAll = cursor.fetchall()

    cursor.close()
    connection.close()

    result = fetchAll[0]

    return result
