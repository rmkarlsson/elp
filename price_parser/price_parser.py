import json
import logging

# Configure logger
logger = logging.getLogger(__name__)

def read_json_string(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None



def get_day_avergare(data):
    total_value = 0
    count = 0

    if isinstance(data, list):
        for item in data:
            if isinstance(item, dict) and "Value" in item:
                total_value += float(item["Value"])
                count += 1

    if count > 0:
        average_value = total_value / count
        logger.debug(f"Calculated average value: {average_value:.2f} öre")
        return average_value/100
    else:
        print("No 'Value' key found in the list of JSON objects")




def convert_to_time_object(time_string):
    try:
        time_object = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S")
        return time_object
    except ValueError as e:
        print(f"Error converting time string: {e}")
        return None

def find_timestamp(data):
    if isinstance(data, dict):
        for key, value in data.items():
            if key == "TimeStamp":
                print(f"Found TimeStamp: {value}")
            else:
                find_timestamp(value)
    elif isinstance(data, list):
        for item in data:
            find_timestamp(item)

    # Example usage
    json_string = '{"event": {"TimeStamp": "2023-10-01T12:00:00Z", "details": {"TimeStamp": "2023-10-01T12:30:00Z"}}}'
    data = read_json_string(json_string)
    if data:
        find_timestamp(data)