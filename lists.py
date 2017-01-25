# a list is a collection of values
# inside a list, order matters!

lister = [1, 2, 4, 'hello']

lister.append(2) # will add 2 to the end of the list

print lister

print lister.index('hello') # will print the index of 'hello' in this case
                            # the index is 3

print lister.count(2) # how many 2's are in the list

# lister.remove(2) would remove the first 2 in the list, you always start from
# the 0th index so the first two is caught and removed instead of the last 2

lister.reverse() # reverses the values in the list

print lister

lister2 = [1,5,6,4,7]

lister2.sort() # sorts lister2 in ascending format

print lister2
