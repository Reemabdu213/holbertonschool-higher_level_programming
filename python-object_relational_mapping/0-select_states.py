#!/usr/bin/python3
"""Script that lists all states from the database"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )

    # Create cursor and execute query
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch and display results
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close connections
    cursor.close()
    db.close()
