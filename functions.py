#function: a group or collection of code that performs a specific task as intended by the user
#when the said function is needed to be performed, the function can be 'called'
#functions help organize code and enable modular programming

#function to say hi to the user

#keyword def : indicates that user is defining a user-defined function
def say_hi():
    print("Hello User! ")
#functions are named with all letters in lower case, and undercore separating two words
#function-calling
say_hi()

#can add additional information to functions by giving them parameters
#can pass in strings, numbers, booleans and other data types into functions
def hello(name, age):
    print("Hello User! " + name + " who is " + str(age) + " years old")
    print("Hola! " + name + " who is " + str(age) + " years old")
hello("Mike",30) #information about parameters is given while calling the function
hello("Steve", 20)



