# Overview

I want to learn how to use SQL databases but work with them using Python code. 

I created an inventory database to track items that a credit union owns. Right now, they are only tracking the computers. Specifically, the information they need is to assign a number to the item, have the name, and location of that item. 

I wanted to write this software to try and see if I could find a way to better track the credit union inventory. 

Below is a software demo video of my code and what I have learned.

[Using Python with SQL Databases Video](https://youtu.be/W9Pyeur7CWU)

# Relational Database

I am using a SQL relational database. 

My table is created hold basic information about an item. The columns are number (primary key), make, model, name, purchased date, and assigned branch. The next table would be monitors and would include that same information.

# Development Environment

I used VS Code to write the program and test it. 

I wrote the program in Python and used the python library SQLite3 to use SQL commands. 

# Useful Websites

This is a list of websites that I found helpful and referenced frequently. 

- [SQLite Tutorial](https://www.sqlitetutorial.net/)
- [Python](https://docs.python.org/3.8/library/sqlite3.html)

# Future Work

This is a list of things that I would like to improve, add, or fix in the future. 

- Create an interface that a user could search, modify, etc. to the database
- Create a second table that I could then perform joins, unions, etc. with
- Fix the layout so that I don't have to comment so much out while I am testing/debugging code