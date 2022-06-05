#Function definition 
def negativeorpositive(a):
  print('a = ' + str(a))
  if int(a) > 0:
    print('a is greater than b ') # print a is a positive number not greater than b.
  elif int(a)==0:
    print('a is equal to b') # a is equal zero not equal b, we do not have b at here
  else:
    print('a is less than b') # a is a negative number.

# main program
a = input('enter number a=')
negativeorpositive(a)