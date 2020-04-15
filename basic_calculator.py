num1 = input('Enter the first number: ') #when we get input from user, by default python converts it into a string
num2 = input('Enter the second number: ')
#answer = num1 + num2 # written this way, its taking the two inputs as strings and ends up only concatenating it, which is obviously not what we want
#so in order to make python understand that these are numbers, we need to convert the string into numbers
# This conversion can be done via two special python functions : int (variable) which is only fo rwhole numbers
#answer = int(num1) + int(num2)
# for using decimal numbers, use the float(variable) function
answer = float(num1) + float (num2)
print(answer)