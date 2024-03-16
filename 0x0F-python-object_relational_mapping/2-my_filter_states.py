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
            SELECT id, name
            FROM states
            WHERE name = '{}'
            ORDER BY id ASC;
            """.format(sys.argv[4].strip('')))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == '__main__':
    main()
