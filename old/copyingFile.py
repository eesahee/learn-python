f = open("sample3.txt")

with open("in.txt") as f:
    with open("out.txt", "w") as out:
        for line in f:      # went through each line and outputted contents to
            out.write(line) # out file. As before files are auto closed
