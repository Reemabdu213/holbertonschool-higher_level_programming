#!/usr/bin/python3
"""Script that displays all values in states table where name matches
argument - safe from SQL injection"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    cursor = db.cursor()
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"
    cursor.execute(query, (sys.argv[4],))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
