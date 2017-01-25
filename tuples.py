# immutable sequence of python objects
# tuples are like lists, but they cannot be changed
# tuples respond to the same operations as strings

tup = ("match", "football", 2005)
tuper = ()
tuper = (1,) # you must have a comma after the first value even if its the only
             # value in the tuple

print tup[0] # this will access the first value
print tup[0:2]  # while this will create a copy of the tuple and give us back
                # index 0 -2 but not including 2

tup1 = (10, 5)
tup2 = ("me", "you")
tup3 = (tup1[0], tup2[0]) # because we cannot modify tuples if we wish to
                          # change them in some way, we must make a new tuple
                          # and put in desired value
print tup3

tuper = ("grades" , 100)
del tuper # tuples cannot be changed but can be deleted
          # print tuper would give us an error becuase it would no longer
          # exist

tuper = (1, 2, 3)

print len(tuper) # prints length of the tuple

print tuper + tuper # concatanate with itself

print tuper * 3 # tuple concatanated 3 times with itelf

print 3 in tuper # is 3 in tuper? in this case, yes.

for x in tuper: # print out the values of the tuple
        print x

lister = [1, 5 ,3]

tuper = tuple(lister) # will convert lister to a tuple

print lister
print tuper # values of lister are now in a tuple

#unpacking

tup = ("Sam", 20)

x , y = tup # seperate the tuple into its parts (unpack)

print x # takes the first value

print y # takes the second value

x ,y = y, x  # swaps the values

print x # x should = y

print y # y should = x
