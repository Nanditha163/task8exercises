# Simple Calculator using try and except
print("Welcome To My Calculator :\n")
print("Math Operations")
print("       +\n" "       -\n" "       *\n" "       /\n")

num1 = float(input("Enter First Number: "))
op = input("Enter Operation: ")
num2 = float(input("Enter Second Number: "))

try:
    val = int(num1)
except ValueError:
    print("Error: Enter A Valid Number")

try:
    val = int(num2)
except ValueError:
    print("Error: Enter A Valid Number")

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1 / num2)
else:
    print("INVALID,please try again!")