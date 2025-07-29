import mysql.connector

def insert_data(id, name, country):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="roottoor",
            database="chandan_ece"
        )
        
        mycursor = mydb.cursor()

        # Insert the data
        sql = "INSERT INTO cities(id, name, country) VALUES (%s, %s, %s)"
        value = (id, name, country)
        mycursor.execute(sql, value)
        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

        # Retrieve and display all records
        mycursor.execute("SELECT * FROM cities")
        result = mycursor.fetchall()
        for row in result:
            print(row)

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if mycursor:
            mycursor.close()
        if mydb:
            mydb.close()

# Get input from the user
id = int(input("Enter the ID: "))  # Ensure ID is an integer
name = input("Enter the name: ")
country = input("Enter the country: ")

insert_data(id, name, country)
