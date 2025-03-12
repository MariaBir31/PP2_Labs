# import json
# from datetime import datetime, timedelta

# current_date = datetime.now()

# new_day = current_date - timedelta(days= 5)

# date_data = {
#     "current_date": current_date.strftime("%Y-%m-%d"),
#     "new_date": new_day.strftime("%Y-%m-%d")
# }

# with open("date.result.json", "w") as file:
#     json.dump(date_data, file, indent=4)

# print(json.dumps(date_data, indent = 4))

from datetime import datetime, timedelta
current_date = datetime.now()

new_date = current_date - timedelta(days=5)

print("Current Date:", current_date.strftime("%Y-%m-%d"))
print("Date 5 Days Ago:", new_date.strftime("%Y-%m-%d"))