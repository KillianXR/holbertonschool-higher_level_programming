#!/usr/bin/python3
"""list all states of a database"""

import MySQLdb
import sys

if __name__ == "__main__":

# input validation
    if len (sys.argv) != 4:
        print("Usage: ./0-select_states.py <mysql_username> <mysql_password> <database_name>")
        sys.exit(1)
    
# get args
    username = sys.argv[1]
    password = sys.argv[2]
    database_name = sys.argv[3]

# connect to database
    database = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database_name)

# cursor creation to interact with the database and display the result
    cursor = database.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)

# close database connexion
    cursor.close
    database.close