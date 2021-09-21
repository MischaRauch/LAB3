from django.db import connection

def my_custom_sql():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM menu_pizza")
    row = cursor.fetchall()
    return row

#def __main__(self):
#     my_custom_sql(self)
#     cursor = connection.cursor()
#     cursor.execute("SELECT * FROM menu_pizza")
#     row = cursor.fetchall()
#     return row

if __name__ == '__main__':
     my_custom_sql()