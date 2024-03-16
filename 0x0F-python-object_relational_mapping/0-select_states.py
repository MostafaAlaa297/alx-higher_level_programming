import MySQLdb
import sys

conn = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3], host="localhost", port=3306)

cur = conn.cursor()

cur.execute("SELECT id, name FROM states ORDER BY states.id ASC")

rows = cur.fetchall()

cur.close()
