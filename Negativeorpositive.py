
def negativeorpositive(a):
  print('a = ' + str(a))
  if int(a) > 0:
    print('a is greater than b ')
  elif int(a)==0:
    print('a is equal to b')
  else:
    print('a is less than b')

a = input('enter number a=')
negativeorpositive(a)