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
# First column is primary key by making it an INTEGER NOT NULL PRIMARY KEY
cur.execute(''' CREATE TABLE computer
               (number INTEGER NOT NULL PRIMARY KEY, make, model, purchasedDate, name, assignedBranch)''')

# Inserting a row of data
cur.execute("INSERT INTO computer VALUES (1, 'Dell', 'Optiplex 7090', '06-17-2023', 'rex01', 'Rexburg')")

# How to do a large insert of rows of data
# using purchases to hold the values
purchases = [(2, 'Dell', 'Optiplex 7090', '06-17-2023', 'rex02', 'Rexburg'),
             (3, 'Dell', 'Optiplex 7090', '06-17-2023', 'rex03', 'Rexburg'),
             (4, 'Dell', 'Optiplex 3080', '04-09-2021', 'ifa01', 'Idaho Falls'),
             (5, 'Dell', 'Optiplex 3080', '04-09-2021', 'ifa02', 'Idaho Falls'),
             ]
# Using the execute many function to insert many rows
# Using the ? symbol as a place holder
# Need 6 placeholders since I have 6 columns
cur.executemany("INSERT INTO computer VALUES (?,?,?,?,?,?)", purchases)

# Save the changes by committing them to our db
con.commit()

# Now, I want to look through my data
# Using a loop to look through all the rows that match my query
# * is a placeholder so that it grabs all of them
for row in cur.execute("SELECT * FROM computer ORDER BY name"):
    print(row)

# Inserting a line break otherwise our queries are too squished.
print('---')

# I accidentally put in a third computer for Rexburg
# The computer actually belongs to Rigby
# I need to update it
cur.execute("UPDATE computer SET name ='rig01', assignedBranch = 'Rigby' WHERE number = 3")
# USED update to tell it we are changing data
# SET to change the right column
# WHERE to tell it what to change

# Save our changes!
con.commit()

# Now, I want to see our changes
for row in cur.execute("SELECT * FROM computer ORDER BY name"):
    print(row)

# Inserting a line break to make the terminal less congested
print('---')

# I messed up again and there are NOT 2 computers in Idaho Falls
# I am going to delete it from our table
# Specify the table and what number needs deleted
cur.execute("DELETE FROM computer WHERE number = 5")

# Save the changes!!!
con.commit()

# We are going to print our table again
for row in cur.execute("SELECT * FROM computer ORDER BY name"):
    print(row)

# Don't forgot to save changes
# Closes the connection if we are done with it
con.close