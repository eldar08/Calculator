def times (x,y):
    return x*y
def division (x,y):
    while y==0:
        return "Cannot be divided by 0."
    return x/y
def plus (x,y):
    return x+y
def minus (x,y):
    return x-y
def power (x,y):
    if x==0 and y<0:
        return "İt cannot be negative number in the power of zero!"
    elif x<0:
        return "İt cannot be a power on a negative number!"
    return x**y
print("1.Times---" "\n" "2.Divide---" "\n" "3.Plus---""\n" "4.Minus---""\n" "5.The power of first number---")
num=int(input("Choose a number to begin: "))
if num==1:
    x=int(input("Enter the first number: "))
    y=int(input("Enter the second number: "))
    result=times(x, y)
    print(result)
elif num==2:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    result = division(x, y)
    print(result)
elif num==3:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    result = plus(x, y)
    #print all results
    print(result)
elif num==4:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    result = minus(x, y)
    print(result)
elif num==5:
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))
    result = power(x, y)
    print(result)
else:
    print("It cannot be defined by our server!")