"""Query the database"""

import sqlite3
from pprint import pprint
import sys

sys.setrecursionlimit(10000)


def query(limit=5):
    """Query the database for the top N rows of the airbnb table"""
    conn = sqlite3.connect("airbnb.db")
    cursor = conn.cursor()
    cursor.execute(
        f"SELECT price, bedrooms, room_type, bathrooms_text FROM airbnb LIMIT {limit}"
    )
    rows = cursor.fetchall()
    print(f"Top {limit} rows of the airbnb table:")
    column_names = [description[0] for description in cursor.description]
    output = [column_names] + [[row[i] for i in range(len(row))] for row in rows]
    pprint(output)
    conn.close()
    return "Success"
