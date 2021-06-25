import psycopg2
from datetime import datetime

conn = psycopg2.connect(
    host="localhost",
    database="notifications",
    user="postgres",
    password="endysoft123")


def create_notification(title: str, description: str, time: datetime, time_before: datetime, type_id: int):
    cur = conn.cursor()
    cur.execute("INSERT INTO notification (title, description, time, time_before, type_id) VALUES (%s, %s, %s, %s, %s)",
                (title, description, time, time_before, type_id))
    cur.close()
    conn.commit()


def update_notification(notification_id: int, type_id: int, title=None, description=None, time=None, time_before=None):
    """
    Dynamically creates UPDATE query with given parameters.
    :param notification_id:
    :param type_id:
    :param title:
    :param description:
    :param time:
    :param time_before:
    :return:
    """
    arguments_dict = {
        "notification_id": notification_id,
        "title": title,
        "description": description,
        "time": time,
        "time_before": time_before,
        "type_id": type_id
    }
    cur = conn.cursor()

    sql = "UPDATE notification SET "
    for key, value in arguments_dict.items():
        if value:
            sql += f"{key} = %({key})s,"
    sql = sql[:-1]
    sql += " WHERE notification_id=%(notification_id)s"
    cur.execute(sql, arguments_dict)
    cur.close()
    conn.commit()


def select_notification(notification_id: int):
    cur = conn.cursor()
    cur.execute("SELECT * FROM notification WHERE notification_id = %s", (notification_id,))
    result = cur.fetchone()
    cur.close()
    return result


def select_notifications():
    cur = conn.cursor()
    cur.execute("SELECT * FROM notification")
    results = cur.fetchall()
    cur.close()
    return results


def remove_notification(notification_id: int):
    cur = conn.cursor()
    cur.execute("DELETE FROM notification WHERE notification_id = %s", (notification_id,))
    cur.close()
    conn.commmit()
