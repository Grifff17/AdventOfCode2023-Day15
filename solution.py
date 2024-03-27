def solvepart1():
    data = fileRead("input.txt")
    steps = data[0].strip().split(",")

    sum = 0
    for step in steps:
        val = 0
        for pos in step:
            val = val + ord(pos)
            val = val * 17
            val = val % 256
        #print(val)
        sum = sum + val
    print(sum)

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart1()