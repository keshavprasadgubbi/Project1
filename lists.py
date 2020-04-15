#usually we end up dealing with large amounts of data; managing and organizing these large amt of data can
#be done via lists! Lists is a structure in python to store list of information
friends = [ "saba","jags",'jags','jags', 'sameer','vasanth'] #list must always be written in square brackets with individual objects written in quotes separated by a comma
#what can be put inside of a list? it can contain strings, numbers and boolean.
print(friends)#prints all the contents of the list
print(friends[2])# with the index being mentioned of the element of the list, with the index starting at 0.
print(friends[-1])#accessing the elements from back of the list, with -1 referring to the last element as the first one in reverse
print(friends[1:])#accessing the elements after a given index
print(friends[1:3])#accessing elements in a given range
friends[2]= 'Nike'#accessing/modifying a specific element of the list
print(friends)

###List functions: .extend(list), .append(element), .insert(index, element), .remove(element)
### .pop(), .clear(), .index(element), .count(element), .sort(), .reverse(),
numbers = [14,5,2,6,3,7,8]
#friends.extend(numbers)# appends one list to another;the first list will have elements of both lists now
print(friends)
friends.append("Ambika")#appends individual elements to the list, but this adds to teh end of the list
friends.insert(3, "Anu")#appends individual element at given index
friends.remove("Nike")#removes a particulat element from list
friends.pop()# removes/pops-out last element of the list
print(friends.index("saba"))#checks if the particular element is present in the list and returns the index of element if available
print(friends.count("jags"))#counts the number of times a given element is repeated
#friends.clear()#completely removes all the elements of the list
friends.sort()# sorts the elements in increasing/alphabetical order. If both text and numbers are present as elements in same list, this will not work; will return an error
numbers.sort()
numbers.reverse()
print(numbers)
print(friends)

best_friends = friends.copy()#copy down entire list
print(best_friends)

