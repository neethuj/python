
import os
import mysql.connector

# Establishing connection to MySQL
cnx =  mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test"
)

# Creating a cursor object
cursor = cnx.cursor()

# CREATE operation with user input
def create():
    id = input("Enter employee id: ")
    name = input("Enter employee Name: ")
    sql = "INSERT INTO employees ( emp_id, emp_name) VALUES (%s, %s)"
    values = (id, name)
    cursor.execute(sql, values)
    cnx.commit()
    print(cursor.rowcount, "record inserted.")

# READ operation
def read():
    cursor.execute("SELECT * FROM employees")
    results = cursor.fetchall()
    for row in results:
        print(row)

# UPDATE operation with user input
def update():
    id = input("Enter employee_id to update: ")
    name = input("Enter employee name: ")
    sql = "UPDATE employees SET emp_name=%s WHERE emp_id=%s"
    values = ( name, id)
    cursor.execute(sql, values)
    cnx.commit()
    print(cursor.rowcount, "record updated.")
# DELETE operation with user input
def delete():
    id = input("Enter id to delete: ")
    sql = "DELETE FROM employees WHERE emp_id=%s"
    value = (id,)
    cursor.execute(sql, value)
    # cursor.execute("DELETE FROM employees WHERE emp_id=%s",(id,))
    cnx.commit()
    print(cursor.rowcount, "record(s) deleted.")

# Main program
while True:
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        create()
    elif choice == "2":
        read()
    elif choice == "3":
        update()
    elif choice == "4":
        delete()
    elif choice == "5":
        break
    else:
        print("Invalid choice.")

# Closing the database connection
cnx.close()