num1 = float(input("Num1:"))
op = input("op:")
num2 = float(input("Num2:"))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "*":
    print(num1 * num2)
elif op == "/":
    print(num1/num2)
else:
    print("invalid operator")
