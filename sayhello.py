from datetime import datetime

hour = datetime.now().time().hour # time object

print("sever time =", hour)
print("type(now) =", type(hour))	

if hour < 12:
    print('Good morning')
    