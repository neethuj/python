import mysql.connector

# Establishing connection to MySQL
db =  mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="test"
)

# Creating a cursor object
cursor = db.cursor()

# CREATE operation with user input
def create():
    name = input("Enter Student Name: ")
    grade = input("Enter Grade: ")
    sql = "INSERT INTO studentinfo ( studentname, studentgrade) VALUES (%s, %s)"
    values = (name, grade)
    cursor.execute(sql, values)
    db.commit()
    print(cursor.rowcount, "record inserted.")

# READ operation
def read():
    cursor.execute("SELECT * FROM studentinfo")
    results = cursor.fetchall()
    for row in results:
        print(row)

# UPDATE operation with user input
def update():
    id = input("Enter id to update: ")
    grade = input("Enter Student Grade: ")
    sql = "UPDATE studentinfo SET studentgrade=%s WHERE studentid=%s"
    values = ( grade, id)
    cursor.execute(sql, values)
    db.commit()
    print(cursor.rowcount, "record updated.")
# DELETE operation with user input
def delete():
    id = input("Enter id to delete: ")
    sql = "DELETE FROM studentinfo WHERE studentid=%s"
    value = (id,)
    cursor.execute(sql, value)
    db.commit()
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
        print("Invalid Choice.")

# Closing the database connection
db.close()