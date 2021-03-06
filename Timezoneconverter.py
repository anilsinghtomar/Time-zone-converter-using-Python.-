import pytz, datetime

year = int(input())
month = int(input())
date = int(input())
hour = int(input())
minute = int(input())

#converting to a date

users_time = datetime.datetime(year,month,date,hour,minute)

kolkata_timezone = pytz.timezone('Asia/Kolkata')
tokyo_timezone = pytz.timezone('Asia/Tokyo')
london_timezone = pytz.timezone('UTC')
sydney_timezone = pytz.timezone('Australia/Sydney')


kolkata_time = pytz.utc.localize(users_time).astimezone(kolkata_timezone)
tokyo_time = pytz.utc.localize(users_time).astimezone(tokyo_timezone)
london_time = pytz.utc.localize(users_time).astimezone(london_timezone)
sydney_time = pytz.utc.localize(users_time).astimezone(sydney_timezone)


print("Kolkata Time is -", kolkata_time.isoformat())
print("Tokyo Time is -", tokyo_time.isoformat())
print("London Time is -", london_time.isoformat())
print("Sydney Time is -", sydney_time.isoformat())
