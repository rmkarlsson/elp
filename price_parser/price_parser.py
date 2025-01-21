import json
import logging
from datetime import datetime

# Configure logger
logger = logging.getLogger(__name__)

def read_json_string(json_string):
    try:
        data = json.loads(json_string)
        return data
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None


def convert_to_time_object(time_string):
    try:
        time_object = datetime.strptime(time_string, "%Y-%m-%dT%H:%M:%S")
        return time_object
    except ValueError as e:
        print(f"Error converting time string: {e}")
        return None


def get_montly_cost(data, consumption, fixed_price):
    total_value = 0
    count = 0
    cost = []
    previous_date = datetime(1970, 12, 1)

    if isinstance(data, list):
        for item in data:

            if isinstance(item, dict) and "TimeStamp" in item:
                date = convert_to_time_object(item["TimeStamp"])
                month_str = date.strftime("%b")
                if date.month != previous_date.month:
                    old_month_str = previous_date.strftime("%b")
                    logger.debug(f"Month changed: {old_month_str} ==> {month_str}")
                    if count > 0:
                        month_avg = (total_value / count)/100
                        count = 0
                        total_value = 0
                        cost.append(int(consumption[old_month_str]) * month_avg)
                        logger.debug(f"Avg for {old_month_str} is {month_avg:.2f} kr/kWh")
                        cost_month = int(consumption[month_str]) * month_avg
                        savings_fixed_cost_month = ((int(consumption[month_str]) * float(fixed_price))/100) - cost_month
                        logger.debug(f'Total cost for {old_month_str} is {int(consumption[month_str]) * month_avg:.2f} kr')
                        logger.debug(f'Savings to fixed price is {savings_fixed_cost_month:.2f} kr based on {(float(fixed_price)/100) - month_avg:.2f} kr/kWh and consumption {int(consumption[month_str])}')


                    previous_date = date


            if isinstance(item, dict) and "Value" in item:
                total_value += float(item["Value"])
                count += 1


        return cost
    else:
        print("No 'Value' key found in the list of JSON objects")





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