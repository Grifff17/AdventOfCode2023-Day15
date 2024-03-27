def solvepart1():
    #read in data
    data = fileRead("input.txt")
    steps = data[0].strip().split(",")

    #calculate hashes
    sum = 0
    for step in steps:
        val = 0
        for pos in step:
            val = val + ord(pos)
            val = val * 17
            val = val % 256
        sum = sum + val
    print(sum)
    

def solvepart2():
    #read in data and initalize boxes
    data = fileRead("input.txt")
    steps = data[0].strip().split(",")
    boxes = [ [] for _ in range(256) ]
    
    #perform initalization sequence
    for step in steps:
        label = ""
        focalLen = 0
        if "=" in step:
            splitStep = step.split("=")
            label = splitStep[0]
            focalLen = int(splitStep[1])
        else:
            label = step[:-1]
        boxIndex = hashAlgorithm(label)
        box = boxes[boxIndex]

        labelExists = False
        index = 0
        for i in range(len(box)):
            if label == box[i][0]:
                labelExists = True
                index = i
                break
        
        if "=" in step:
            if labelExists:
                box[index][1] = focalLen
            else:
                box.append([label, focalLen])
        else:
            if labelExists:
                del box[index]

    #calculate focusing power
    sum = 0
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            fp = (1+i) * (1+j) * (boxes[i][j][1])
            sum = sum + fp
    print(sum)

            


#run hash algorithm on a sring
def hashAlgorithm(input):
    val = 0
    for pos in input:
        val = val + ord(pos)
        val = val * 17
        val = val % 256
    return val

def fileRead(name):
    data = []
    f = open(name, "r")
    for line in f:
        data.append(line);
    return data

solvepart2()