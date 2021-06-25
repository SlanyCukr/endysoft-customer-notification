from flask import Flask

app = Flask(__name__)


@app.route("/new_notification", methods=['POST'])
def new_notification():
    return "ok"


@app.route("/change_notification", methods=['PUT'])
def change_notification():
    return "ok"


@app.route("/get_notification/<notification_id>", methods=['GET'])
def get_notification(notification_id):
    return "ok"


@app.route("/get_notifications", methods=['GET'])
def get_notifications():
    return "ok"


@app.route("/delete_notification", methods=['DELETE'])
def delete_notification():
    return "ok"


@app.route("/send_notification", methods=['GET'])
def send_notification():
    return "ok"


if __name__ == '__main__':
    app.run(debug=True, port=5050)
