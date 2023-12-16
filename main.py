f = open('l.txt')

ints = []

try:
    for line in f:
        ints.append(int(line))
except ValueError:
    print("eto ne chislo")
except:
    print("all good")
finally:
    f.close()
    print("file closed")