from datetime import datetime, timedelta;

x = datetime.now()
y = x - timedelta(days = 1)
c = x + timedelta(days = 1)
print(x, y, c)