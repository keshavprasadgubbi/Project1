print("Giraffe Academy ")
#creating a string variable
phrase = "Elephant Academy"
print(phrase + " is awesome!") #can only conctenate string variables

#Functions : Little block of code that we can run and will
# perform a specific operation for us; can use functions to
#modify our strings or get information about our strings

#to call a function use .function_name()

# common preexisting string variable related functions :
# .lower(),.upper()
#to check if the string is given way or not, can use many .is_functionname() and will return a true or false value
#can use these functions in combinations with each other

print(phrase.lower())
print(phrase.upper())
print(phrase.islower())
print(phrase.lower().isupper())
print(phrase.upper().isupper())
#can figure out length of the string with len() function; can also get the individual
#character via the index with string_variable[obj], with index starting with 0
print(len(phrase))
print(phrase[10])
# .index() function is useful for passing the parameters as arguments to the function
# and will return the value at its particular index
print(phrase.index("Aca"))
# .replace(old_str, new_str) function
print(phrase.replace("Academy", "is Cute!"))