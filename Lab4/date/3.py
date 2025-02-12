import json
from datetime import datetime

now = datetime.now()

now_without_microseconds = now.replace(microsecond=0)

date_data = {
    "original_datetime": now.strftime("%Y-%m-%d %H:%M:%S.%f"),  # With microseconds
    "datetime_without_microseconds": now_without_microseconds.strftime("%Y-%m-%d %H:%M:%S")  # Without microseconds
}

with open("datetime.json", "w") as file:
    json.dump(date_data, file, indent=4)

print(json.dumps(date_data, indent=4))
