#!/usr/bin/python3
"""  Print lists all states from database hbtn_0e_0_usa """
import MySQLdb
import sys


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT cities.name\
            FROM cities JOIN states\
            ON states.id=cities.state_id\
            WHERE states.name=%s\
            ORDER BY cities.id ASC", (sys.argv[4],))
    states = cur.fetchall()
    tp = list(state[0] for state in states)
    print(*tp, sep=", ")
    cur.close()
    db.close()
