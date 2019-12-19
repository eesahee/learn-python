file = open("sample1.txt", "w")
file.write("Hello my name is Isai\nWhat's yours?")
file.close() # You must close the file or else the write does not work


#  OR

with open("sample1.txt", w) as file:
    file.write("Hello my name is Isai\nWho are you?") # file is auto closed
