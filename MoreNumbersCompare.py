# This is function defination.
def compareFuction(a,b,c):  
  if a > b:
    if a > c:
       print('a is biggest number')
    else: # a<c
      print('c is biggest number')
  elif b > c: # a < b
    print('b is biggest number')
  else: # a<b<c
    print('c is biggest number')


# This is the main program, it start run from here when you start
print('USE REAL NUMBERS OR ELSE IT WILL NOT WORK')
a = input('enter number a=')
b = input('enter number b=')
c = input('enter number c=')
# Call the function with real variable values input from user, function will run.
compareFuction(a, b, c)


