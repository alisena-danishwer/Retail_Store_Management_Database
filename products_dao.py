from sql_connection import get_sql_connection

def get_all_products(connection):
    cursor = connection.cursor()
    query = ("SELECT ProductID, ProductName, Category, Price, StockQuantity FROM Products")
    cursor.execute(query)
    response = []
    for (ProductID, ProductName, Category, Price, StockQuantity) in cursor:
        response.append({
            'ProductID': ProductID,
            'ProductName': ProductName,
            'Category': Category,
            'Price': Price,
            'StockQuantity': StockQuantity
        })
    return response

def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("INSERT INTO Products "
             "(ProductName, Category, Price, StockQuantity)"
             "VALUES (%s, %s, %s, %s)")
    data = (product['ProductName'], product['Category'], product['Price'], product['StockQuantity'])

    cursor.execute(query, data)
    connection.commit()

    return cursor.lastrowid

def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = ("DELETE FROM Products WHERE ProductID = %s")
    cursor.execute(query, (product_id,))
    connection.commit()

    return cursor.lastrowid

if __name__ == '__main__':
    connection = get_sql_connection()
    # Test fetching all products
    # print(get_all_products(connection))
    
    # Test inserting a new product
    print(insert_new_product(connection, {
        'ProductName': 'Gaming Mouse',
        'Category': 'Accessories',
        'Price': 59.99,
        'StockQuantity': 150
    }))
