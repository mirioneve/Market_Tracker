# 1. basic of conditionals
num = int(input("Enter Your Number:"))

if num % 2 == 0:
    print("is even")
else:
    print("is Odd")

# 2. Simple Calculator

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Secound Number: "))
operator = input("Enter  Operator: ")

if operator == "+":
    print(num1+num2)
elif operator == "-":
    print(num1-num2)
elif operator == "*":
    print(num1*num2)
elif operator == "/":
    if num2 == 0:
        print("Cannot divide by Zero")
    else:
        print(num1/num2)
else:
    print("choose Your Numbers and an operator ")

