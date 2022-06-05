from datetime import datetime

hour = datetime.now().time().hour # time object

print("sever time =", hour)
print("type(now) =", type(hour))	


def sayhello(hour):
  if hour < 12:
     print('Good morning')
  elif hour <18:
    print('Good afternoon')
  else:
    print('Good night!')

sayhello(hour)
sayhello(14)
sayhello(20)