from math import * #importing prewritten code from math module
print(22.09786)
my_num = -5
print(my_num)
print(5 + my_num)
#converting numbers into a string; then can apply string functions and string operations
print(str(my_num) + " is the new number")
# if my_num isnt converted to string, then python wont accept since numbers cannot be conctenated
#so for printing numbers next to a string, use the str() function

#Math functions - abs(variable), pow(num1, num2), max(num1, num2), min(num1, num2), round(variable),
# floor(variable),
print(abs(my_num))
print(pow(2,3))
print(pow(my_num, 2))
print(max(34,92)) # returns the larger of the two numbers passed in to it as parameters
print(min(34,92)) # returns the smaller of the two numbers passed in to it as parameters
print(round(22.22, 1)) #the second parameter gives the max number of digits that needs to be rounded to

#To  access lot more predefined functions, can import these functions; In python can import
# external code from the 'import' command
print(floor(22.2222263567467))
print(ceil(22.4535))
print(sqrt(22.4543))
print(floor(sqrt(45245.434134)))
