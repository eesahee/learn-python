
while True:
    try:
        x = int(raw_input("Ammount: "))
        break
    except ValueError:
        print ("Enter valid number")

try :
    x = int(raw_input("Ammount: "))
except ValueError:
    print "Value"
except RuntimeError, TypeError:
    print "other"
