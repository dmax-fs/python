#R1-1 - solved, not exact solution

#m = int(input("Please enter first number: "))
#n = int(input("Please enter second number: "))
#if m % n == 0:
#    print(bool(True))
#else:
#    print(bool(False))
    
#R1-2 - solved, not exact solution - using modulo

#k = input("Please enter a number: ")
#k = int(k)
#def is_even(k):
#    if k % 2 == 0:
#        print (bool(True))
#    else:
#        print (bool(False))
#    return k
#print(str(is_even(k)) + " is " ) # need to print odd or even in result

#R1-2 - another solve, not exact solution - using modulo

number = input("Please enter a number: ")
number = int(number)

def isEven(number):
    return number % 2 == 0

if (isEven(number) == True):
    print(str(number) + " is even")
else:
    print(str(number) + " is odd")

#R1-3 - in progress
