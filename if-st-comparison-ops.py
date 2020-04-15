#if statement and comparison operators
#instead of statements, can use comparison as conditions for if statements
#create a function that gives the maximum number that we pass into it
#take in 3 parameters as input and print out biggest number as output

def max_num(num1, num2, num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(14,52,9))
