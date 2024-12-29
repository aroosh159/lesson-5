def intro(name):
    print("Hello Good morning,My name is ",name)
user_name = input("Enter your name: ")
intro(user_name)

#Checking factorial of a number

def recurr_factorial(n):
    if n == 1:
        return n
    else:
        return n*recurr_factorial(n-1)
num = int(input("Enter your number:"))
if num<0:
    print("Sorry!Factorial doesnot exist for Negative Numbers")
elif num==0:
    print("The Factorial of 0 is 1")
else :
    print("The Factorial of ",num ,"is ",recurr_factorial(num))

#Making a simple calculator
def add(x,y):
   return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
num1 = int(input("Enter your number:"))
num2 = int(input("Enter your number:"))
print("Sum",add(num1,num2))
print("Difference",subtract(num1,num2))
print("Product",multiply(num1,num2))
print("Quotient",divide(num1,num2))