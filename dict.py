# dictionaries are sets of key- value pairs

dictionary = {}

tel = {"Mary" : 4156, "John": 4512, "Jerry": 5555}

print tel

tel['Jane'] = 5432 # inserts a new specific key-value

print tel

print tel['Jerry'] # looks up the value for the Key "Jerry"

del tel['Jerry'] # remove Jerry since he is no longer our friend

print tel # Jerry should not show up anymore
