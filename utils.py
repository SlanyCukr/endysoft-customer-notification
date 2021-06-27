import datetime
import json
import time

notification_type_names = ["notification_id", "title", "description", "time", "time_before", "type_id"]


def get_ok_message(message=None):
    return json.dumps({"status": "ok", "message": message})


def get_error_message(message=None):
    return json.dumps({"status": "error", "message": message})


def database_result_into_str(result):
    temp_zip = list(zip(notification_type_names, result))

    created_obj = {}
    for key_value in temp_zip:
        if type(key_value[1]) == datetime.datetime:
            created_obj[key_value[0]] = time.mktime(key_value[1].timetuple())
        else:
            created_obj[key_value[0]] = key_value[1]
    return created_obj


def database_results_into_list(results):
    lst = []
    for result in results:
        lst.append(database_result_into_str(result))
    return lst
