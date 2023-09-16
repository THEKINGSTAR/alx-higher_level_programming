#!/usr/bin/python3
"""
SCRIPT Takes in an argument and displays all values
in the states table of hbtn_0e_0_usa where name matches the argument.
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=mysql_username,
                         port=3306, password=mysql_password,
                         database=database_name)

    cur = db.cursor()

    query = """SELECT cities.id, cities.name , states.name
            FROM cities
            LEFT JOIN states
            ON cities.state_id = states.id
            ORDER BY cities.id ASC;"""

    cur.execute(query)

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
