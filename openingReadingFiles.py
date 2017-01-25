f = open("sample.txt", "r")
quote = f.read()

print quote

f.seek(0) # points back to the beginning of the file

print f.read() # now we can read from the top again

f.close() # will now close the file
