from datetime import datetime

date1 = datetime(2025, 2, 10, 12, 0, 0)
date2 = datetime(2025, 2, 14, 14, 30, 0)

difference_in_seconds = abs((date2 - date1).total_seconds())

print("Date 1:", date1)
print("Date 2:", date2)
print("Difference in Seconds:", difference_in_seconds)