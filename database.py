# Import sqlite3 which I will be using to create my database
import sqlite3

# Next I need to connect to the database inorder to work with it
# Looks like conn = sqlite3.connect('databasename')
con = sqlite3.connect('inventory.db')

# Confirm that it was opened with the print statement
print("Opened database successfully.");

# Calling the cursor obeject to be able to use the execute method
cur = con.cursor()

# Creating my first table using the execute method
# Then the rows are listed as well
#cur.execute(''' CREATE TABLE computer
#               (make, model, purchased date, name, branch assigned)''')

# Inserting a row of data
cur.execute("INSERT INTO computer VALUES ('Dell', 'Optiplex 7090', '06-17-2023', 'rex01', 'Rexburg')")

# How to do a large insert of rows of data
# using purchases to hold the values
purchases = [('Dell', 'Optiplex 7090', '06-17-2023', 'rex02', 'Rexburg'),
             ('Dell', 'Optiplex 7090', '06-17-2023', 'rex03', 'Rexburg'),
             ('Dell', 'Optiplex 3080', '04-09-2021', 'ifa01', 'Idaho Falls'),
             ('Dell', 'Optiplex 3080', '04-09-2021', 'ifa02', 'Idaho Falls'),
             ]
# Using the execute many function to insert many rows
# Using the ? symbol as a place holder
# Need 5 placeholders since I have five columns
cur.executemany("INSERT INTO computer VALUES (?,?,?,?,?)", purchases)


# Save the changes by committing them to our db
con.commit()

# Don't forgot to save changes
# Closes the connection if we are done with it
con.close