import sqlite3

db = sqlite3.connect("company.db")
cur = db.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
table_list = cur.fetchall()

table_schema = {}

for t in table_list:
    name = t[0]
    cur.execute("PRAGMA table_info(" + name + ")")
    cols = []

    for c in cur.fetchall():
        cols.append(c[1])   

    table_schema[name] = cols

print("\nTables and their Columns:\n")

for table in table_schema:
    print(table, "->", table_schema[table])

print("\nPossible Optimized Joins:\n")

unique_joins = []

for t1 in table_schema:
    for t2 in table_schema:

        if t1 >= t2:
            continue

        for col in table_schema[t1]:

            if col in table_schema[t2] and col.endswith("_id"):

                join_text = t1 + "." + col + " = " + t2 + "." + col

                if join_text not in unique_joins:
                    unique_joins.append(join_text)
                    print(join_text)

print("\nPerformance Suggestions:\n")

for table in table_schema:
    for col in table_schema[table]:

        if col.endswith("_id"):
            print("Add INDEX on", table + "." + col)
            print("Use INNER JOIN when joining on", col)

db.close()
