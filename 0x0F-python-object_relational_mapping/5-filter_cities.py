#!/usr/bin/python3

"""
Get state ids and names
"""

import MySQLdb
import sys


def main():
    """
    Main funtion
    """
    conn = MySQLdb.connect(
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            host="localhost",
            port=3306
            )

    cur = conn.cursor()

    cur.execute("""
            SELECT cities.name
            FROM cities
            JOIN states ON cities.state_id = states.id
            WHERE states.name = %s
            ORDER BY cities.id ASC;
            """, (sys.argv[4],))

    rows = cur.fetchall()

    for i, row in enumerate(rows):
        if i < len(rows) - 1:
            print(row[0], end=", ")
        else:
            print(row[0])

    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
