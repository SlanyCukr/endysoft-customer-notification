from flask import Flask, request

from database.queries import create_notification, update_notification, select_notification, select_notifications, remove_notification
from utils import *

app = Flask(__name__)


@app.route("/new_notification", methods=['POST'])
def new_notification():
    try:
        title = request.args['title']
        description = request.args['description']
        time = datetime.datetime.fromtimestamp(int(request.args['time']))
        time_before = datetime.datetime.fromtimestamp(int(request.args['time_before']))
        type_id = int(request.args['type_id'])
    except:
        return get_error_message("Couldn't read some of the parameters.")
    else:
        create_notification(title, description, time, time_before, type_id)
        return get_ok_message('Successfully created notification.')


@app.route("/change_notification", methods=['PUT'])
def change_notification():
    try:
        notification_id = int(request.args['notification_id'])
        type_id = int(request.args['type_id'])

        title = request.args.get('title')
        description = request.args.get('description')
        time = request.args.get('time')
        time_before = request.args.get('time_before')

        if time:
            time = datetime.datetime.fromtimestamp(int(time))
        if time_before:
            time_before = datetime.datetime.fromtimestamp(int(time_before))
    except:
        return get_error_message("Couldn't read some of the parameters.")
    else:
        update_notification(notification_id, type_id, title, description, time, time_before)
        return get_ok_message("Successfully updated notification with your values.")


@app.route("/get_notification/<notification_id>", methods=['GET'])
def get_notification(notification_id: int):
    notification = select_notification(notification_id)
    return get_ok_message(json.dumps(database_result_into_str(notification)))


@app.route("/get_notifications", methods=['GET'])
def get_notifications():
    notifications = select_notifications()
    return get_ok_message(json.dumps(database_results_into_list(notifications)))


@app.route("/delete_notification", methods=['DELETE'])
def delete_notification():
    notification_id = int(request.args['notification_id'])
    remove_notification(notification_id)
    return get_ok_message("Successfully removed notification.")


@app.route("/send_notification", methods=['GET'])
def send_notification():
    return "ok"


if __name__ == '__main__':
    app.run(debug=True, port=5050)
