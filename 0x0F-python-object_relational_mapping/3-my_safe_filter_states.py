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
    state_name_searched = sys.argv[4]

    db = MySQLdb.connect(host="localhost", user=mysql_username,
                         port=3307, password=mysql_password,
                         database=database_name)

    cur = db.cursor()

    query = """SELECT *  FROM states
            WHERE name = %s
            ORDER BY states.id ASC;"""

    cur.execute(query, (state_name_searched,))

    results = cur.fetchall()

    for row in results:
        print(row)

    cur.close()
    db.close()
