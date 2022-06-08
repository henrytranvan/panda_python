#This the the code to make the compare possable
def compareFuction(a,b):
  print('a = ' + str(a))
  print('a =' + str(b))
  if a>b:
    print('a is greater than b ')
  elif a==b:
    print('a is equal to b')
  else:
    print('a is less than b')
#This is where the user inputs and tells how big or small a is to b
a = input('enter number a=')
b = input('enter number b=')
compareFuction(a, b)