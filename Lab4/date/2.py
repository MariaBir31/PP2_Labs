import json
from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

date_data = {
    "yesterday": yesterday.strftime("%Y-%m-%d"),
    "today": today.strftime("%Y-%m-%d"),
    "tomorrow": tomorrow.strftime("%Y-%m-%d")
}

with open("dates.json", "w") as file:
    json.dump(date_data, file, indent=4)

print(json.dumps(date_data, indent=4))
