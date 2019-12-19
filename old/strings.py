hello = "hello world"

print(hello[0]) # this will print the "0th" character in a string which is the
                # first character since the index starts at 0 not 1

print(hello[0:4]) # will print from first character up to and not including
                  # the 4. This will print out 'hell'

print hello + " " + hello # The '+' operator will concatanate both strings

print (hello + " ") * 3 # Will concatanate itself  3 times

print "he" in "hello" # Returns a boolean statement if the first string is
                      #  contained in the second one

print "w" in "hello" # w is not found in hello so should return False
