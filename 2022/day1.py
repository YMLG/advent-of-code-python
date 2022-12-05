from os import path
file_path = path.realpath("2022/resources/input1.txt")
#===================*============================
calories = open(file_path, "r")
max = 0
current = 0
for c in calories :
    if(c != "\n"):
        current += int(c) 
    else:
        if(max < current) :
            max = current
        current = 0

print(max)
calories.close();
#===================* *============================
calories = open(file_path, "r")
max = [0, 0 ,0]
current = 0
for c in calories :
    if(c != "\n"):
        current += int(c) 
    else:
        if(max[0] < current) :
            max[2] = max[1]
            max[1] = max[0]
            max[0] = current
        elif(max[1] < current) :
            max[2] = max[1]
            max[1] = current
        elif(max[2] < current) :
            max[2] = current
        current = 0

print(max[0]+max[1]+max[2])
calories.close();