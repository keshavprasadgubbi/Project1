#sometimes when we do function call, we also want information back from the function,
# and not just have the function perform a specific task;hence return statements are helpful to retrive information from function

#create a function to cube a given number
def cubed(num):
    return num*num*num # without using a return st here, python will produce teh answer as none
print(cubed(5))# directly also can do the function-call

#method2: my soln
def cube(num1, num2):
    return(pow(num1, num2))
answer = cube(5,3)# callng the function by assigning parameters to the function and then assigning the answer to a new variable
print(answer)

#Note: no code can be added after including the return statement in the function
#as python interpreter will break out of the function after executing return statement

