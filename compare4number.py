# This is function defination.
def compare3NumberFuction(a,b,c,d):  
    max = a
    if b > max :
        max = b
    if c > max :
        max = c
    if d > max :
        max = d

    return max


# This is the main program, it start run from here when you start
print('USE REAL NUMBERS OR ELSE IT WILL NOT WORK')
a = input('enter number a = ')
b = input('enter number b = ')
c = input('enter number c = ')
d = input('enter number d = ')
# Call the function with real variable values input from user, function will run.
max1 = compare3NumberFuction(a, b, c,d)

print('biggest number is ' + max1)