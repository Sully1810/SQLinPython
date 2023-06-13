# Import sqlite3 which I will be using to create my database
import sqlite3

# Next I need to connect to the database inorder to work with it
# Looks like conn = sqlite3.connect('databasename')
conn = sqlite3.connect('inventory.db')

# Confirm that it was opened with the print statement
print("Opened database successfully.");