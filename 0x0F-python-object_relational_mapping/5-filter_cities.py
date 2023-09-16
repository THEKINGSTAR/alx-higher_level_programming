#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=mysql_username,
                         port=3306, password=mysql_password,
                         database=database_name)

    cur = db.cursor()

    query = """SELECT cities.name
            FROM cities
            LEFT JOIN states
            ON cities.state_id = states.id
            WHERE states.name LIKE BINARY %s
            ORDER BY cities.id ASC;"""

    cur.execute(query, (state_name,))

    results = cur.fetchall()

    for row in results:
        print(row[0], end=' ')
    print('')

    cur.close()
    db.close()
