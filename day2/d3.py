import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('mydata.db')
cursor = conn.cursor()

# Create a table if it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL
)
''')

# Get user input
n=int(input("enter the number of users you want to add:"))
for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))

# Insert the input into the database
    cursor.execute(
    "INSERT INTO user (name, age) VALUES (?, ?)", (name, age))

# Commit the changes and close the connection
    conn.commit()
    conn.close()

print("Data inserted successfully!")
