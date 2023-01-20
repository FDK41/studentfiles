import datetime


weekDays = ("Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday")

 
today    = datetime.date(2023,10,28)

tomorrow = today+datetime.timedelta(days=1)

print(tomorrow.strftime('%A'))
print(today.strftime('%A'))
# print(today.strftime('%A'))
# toDay = today.weekday() #Thursday

# print(toDay)

# toDayAsString = weekDays[toDay]

# print(toDayAsString)
 

# print("today {}".format(toDayAsString))