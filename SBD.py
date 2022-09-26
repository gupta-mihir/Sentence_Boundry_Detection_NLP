print ("Hello World!")
with open('SBD.train.txt') as f:
    lines = f.read(1000)
    print(lines, end='')