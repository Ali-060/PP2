# 1
import datetime
current_date = datetime.datetime.now()
five_days_ago = current_date - datetime.timedelta(days=5)
print("Current Date:", current_date)
print("Five Days Ago:", five_days_ago)

# 2
import datetime
today = datetime.datetime.now()
yesterday = today - datetime.timedelta(days=1)
tomorrow = today + datetime.timedelta(days=1)
print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

# 3
import datetime
current_datetime = datetime.datetime.now()
datetime_without_microseconds = datetime.datetime(
    current_datetime.year,
    current_datetime.month,
    current_datetime.day,
    current_datetime.hour,
    current_datetime.minute,
    current_datetime.second
)
print("Current Datetime:", current_datetime)
print("Datetime without Microseconds:", datetime_without_microseconds)

# 4
import datetime
date1 = datetime.datetime(2023, 5, 10, 12, 30, 0)
date2 = datetime.datetime(2023, 5, 5, 8, 45, 0)
difference_in_seconds = (date1 - date2).total_seconds()
print("Difference in Seconds:", difference_in_seconds)
