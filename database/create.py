import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="notifications",
    user="postgres",
    password="endysoft123")

cur = conn.cursor()

cur.execute("""CREATE TABLE notification_type (
type_id SERIAL PRIMARY KEY,
name VARCHAR(50) NOT NULL
);""")

cur.execute("INSERT INTO notification_type (name) VALUES ('important'), ('normal'), ('low-priority');")

cur.execute("""CREATE TABLE notification (
notification_id SERIAL PRIMARY KEY,
title VARCHAR(100) NOT NULL,
description VARCHAR(100) NOT NULL,
time TIMESTAMP NOT NULL,
time_before TIMESTAMP NOT NULL,
type_id INT NOT NULL,
CONSTRAINT fk_type FOREIGN KEY (type_id) REFERENCES notification_type(type_id)
);""")

cur.close()
conn.commit()
conn.close()
