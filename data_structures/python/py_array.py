# Lists perform the same function as arrays in python.
# Lists are mutable data structures.
# Lists can contain any mix of data types in python.

# Initializing List
mylist = [0]
# Populating list
mylist += [1,3,'some string',4,'a']
mylist.append('appended')

print('Elements added: ', mylist)

# Removing last element
mylist.pop()
# Removing elements from list
mylist.remove(1)
mylist.remove('some string')

print('Elements removed: ', mylist)

# Accessing second element in list (index 1)
print('Accessing: ', mylist[1])