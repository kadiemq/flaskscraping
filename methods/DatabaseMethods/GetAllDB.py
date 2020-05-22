def GetAllDB(check_for):
    if check_for == 'product':
        query = f"select * from product"
    else:
        query = f"select * from user_table"