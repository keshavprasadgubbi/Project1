#Condtionals:
#create a boolean variable whether or not the user is a male
is_male = False
is_tall = False
is_dark = True
if is_male:
    print("User is a male!")
    #nested if statement
    if is_tall:
        print(" and is also tall")
else:
    print("User is female!")
    if is_tall:
        print(" and is also tall")
#multiple conditions in a if statement: using keywords 'and' 'or'
#when  using and, all the conditions placed must be satisfied
if is_male and is_tall and is_dark:
    print("User is Tall, male and dark")
#when using or, if one of the conditions holds, then the if st is executed
if is_male or is_dark:
    print("User is dark male")

#elif ,and ,not:
if is_male and is_tall:
    print("Is a tall male")
elif is_male and not(is_tall):
    print("short male")
elif not(is_male) and not(is_tall):
    print("Short female")
else:
    print("Is either not male or not tall")
