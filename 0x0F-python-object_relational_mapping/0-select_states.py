#!/usr/bin/python3
"""
MODULE TO  lists all states from the database hbtn_0e_0_usa:
"""
if __name__ == "main":
    import MySQLdb
    import sys

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(host="localhost", user=mysql_username,
                         port=3307, password=mysql_password,
                         database=database_name)

    cur = db.cursor()

    query = """SELECT name FROM states
            ORDER BY id ASC"""
    cur.execute(query)

    results = cur.fetchall()

    for idx, row in enumerate(results, start=1):
        print("({}, '{}')".format(idx, row[0]))

    cur.close()
    db.close()