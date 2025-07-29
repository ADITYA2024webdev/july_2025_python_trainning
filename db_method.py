# def insertdata():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     city = input("Enter your city: ")
#     print("\n")
#     print("Your details are: ")
#     print("Name: ", name)
#     print("Age: ", age)
#     print("City: ", city)
#     insertdata()



# def updatedata():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     city = input("Enter your city: ")
#     print("\n")
#     print("Your details are: ")
#     print("Name: ", name)
#     print("Age: ", age)
#     print("City: ", city)
#     updatedata()


# def deletedata():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     city = input("Enter your city: ")
#     print("\n")
#     print("Your details are: ")
#     print("Name: ", name)
#     print("Age: ", age)
#     print("City: ", city)
#     deletedata()
   


# def selectdata():
#     name = input("Enter your name: ")
#     age = int(input("Enter your age: "))
#     city = input("Enter your city: ")
#     print("\n")
#     print("Your details are: ")
#     print("Name: ", name)
#     print("Age: ", age)
#     print("City: ", city)
#     selectdata()









# def insertData(id,name ,password,phoneno,email):
#     sql="insert into user (id,name,password,phoneno,email) values (%s,%s,%s,%s,%s)"
#     val = ( id,name,password,phoneno,email )
#     cursor.execute(sql,val)
#     mydb.commit()
#     cursor.close()
#     mydb.close()


# print(mydb)



from db_config import getDb
class DbMethods:
    def deleteData(self,id):
        try:
            # SQL query to delete data based on id
            sql = "DELETE FROM user WHERE id = %s"
            val = (id,)
            
            # Execute the delete query
            cursor.execute(sql, val)
            
            # Commit the changes
            mydb.commit()

            # Check if any rows were affected (i.e., if any user was deleted)
            if cursor.rowcount > 0:
                print(f"User with ID {id} deleted successfully.")
            else:
                print(f"No user found with ID {id}.")
        
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        
        finally:
            pass
        
    def selectData(self,id=None):
        try:
            if id:
                # Select a specific user
                sql = "SELECT * FROM user WHERE id = %s"
                cursor.execute(sql, (id,))
            else:
                # Select all users
                sql = "SELECT * FROM user"
                cursor.execute(sql)

            results = cursor.fetchall()
            if results:
                print("\nUser Data:")
                for row in results:
                    print(f"ID: {row[0]}, Name: {row[1]}, Password: {row[2]}, Phone: {row[3]}, Email: {row[4]}")
            else:
                print("No user(s) found.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            pass


    def insertData (self,id,name,password,phoneno,email):
        mydb=getDb()
        mycursor =mydb.cursor()
        sql = "INSERT INTO user (id, name, password, phone, email) VALUES ( %s, %s, %s, %s, %s )"
        val = (id,name,password,phoneno,email)
        mycursor.execute(sql, val)

        mydb. commit()
        mycursor.close()
        mydb.close()
        print(" Data inserted successfully into MySQL database", (id,name,password,phoneno,email))
