#!/usr/bin/python3

import MySQLdb
import sys

mysql_username = sys.argv[1]
mysql_password = sys.argv[2]
database_name = sys.argv[3]

db = MySQLdb.connect(host="localhost", user=mysql_username,
                        port=3307, password=mysql_password,
                        database=database_name)

cur = db.cursor()

query = """SELECT *  FROM states
        WHERE name like BINARY 'N%'
        ORDER BY states.id ASC;"""

cur.execute(query)

results = cur.fetchall()

for row in results:
    print(row)

cur.close()
db.close()