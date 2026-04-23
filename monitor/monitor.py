import requests
import time


monitor_url = "http://api:8000/view_all_experiments"


while True:
    try:
        response = requests.get(monitor_url)
        response.raise_for_status()
        check_data= response.json()
        if isinstance(check_data, dict):
            print("SERVICE HEALTHY. Total experiments present is 0")
        elif isinstance(check_data, list):
            count_data = len(check_data)
            print(f"SERVICE HEALTHY. Total experiments present is : {count_data}")
    except requests.exceptions.RequestException as e:
        print(f"SERVICE DOWN. Error: {e}")

    time.sleep(10)

