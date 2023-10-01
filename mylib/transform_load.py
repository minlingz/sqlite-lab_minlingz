"""
Transforms and Loads data into the local SQLite3 database

"""
import sqlite3
import csv


def load(dataset="dataset/listings.csv"):
    """Transforms and Loads data into the local SQLite3 database"""

    with open(dataset, newline="") as csvfile:
        reader = csv.reader(csvfile)
        columns = next(reader)

    with sqlite3.connect("airbnb.db") as conn:
        conn.execute("DROP TABLE IF EXISTS airbnb")

        # generate CREATE TABLE statement dynamically
        create_table = f"CREATE TABLE airbnb ({', '.join(columns)})"
        conn.execute(create_table)

        # insert data into table
        with open(dataset, newline="") as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # skip header row
            for row in reader:
                # remove $ from price column
                row[40] = row[40].replace("$", "")
                placeholders = ",".join(["?"] * len(row))
                insert_stmt = f"INSERT INTO airbnb VALUES ({placeholders})"
                conn.execute(insert_stmt, row)

    return "airbnb.db"
