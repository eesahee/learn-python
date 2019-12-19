# Break, when called,  will exit out of the smallest enclosing for or while
# loop
# Continue , when called, ignore the remaining statements inside of the loop
# and go to the next iteration
# Pass, when called,  = do nothing

var = 10

while True:
    var -= 1
    if var == 6:
        continue # will not print out 6
    print var
    if var == 0 :
        break

print ("Done loop")

for x in range(3):
    pass # should not do anything
