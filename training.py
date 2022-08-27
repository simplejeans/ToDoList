from datetime import datetime, timedelta

for i in range(0, 7):
    today = datetime.today()
    tomorrow = today + timedelta(days=i)
    print(tomorrow)
