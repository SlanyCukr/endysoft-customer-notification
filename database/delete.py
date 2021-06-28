import psycopg2

conn = psycopg2.connect(
    host="postgres",
    database="notifications",
    user="postgres",
    password="endysoft123")

cur = conn.cursor()

cur.execute("DROP TABLE notification")
cur.execute("DROP TABLE type")

cur.close()
conn.commit()
conn.close()
