#!/usr/bin/python3

import MySQLdb
import sys

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

db = MySQLdb.connect(host="localhost",user = mysql_username, port = 3307,password = mysql_password, database = database_name)

db.query("""SELECT states FROM hbtn_0e_0_usa
         WHERE name "like "N.%""")


