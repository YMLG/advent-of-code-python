from os import path
file_path = path.realpath("2022/resources/input2.txt")

#===================*============================
def get_score(a, b):
    if(a == "A") :
        if(b == "X"): return 1 + 3
        elif(b == "Y"): return 2 + 6
        elif(b == "Z"):  return 3 + 0
    elif(a == "B") :
        if(b == "X"): return 1 + 0
        elif(b == "Y"): return 2 + 3
        elif(b == "Z"):  return 3 + 6
    elif(a == "C") :
        if(b == "X"): return 1 + 6
        elif(b == "Y"): return 2 + 0
        elif(b == "Z"):  return 3 + 3

instructions = open(file_path, "r")
score = 0
for i in instructions :
    split = i.split()
    score += get_score(split[0], split[1])
 
print(score)
instructions.close();   
#===================* *============================
def get_score(a, b):
    if(a == "A") :
        if(b == "X"): return 3 + 0
        elif(b == "Y"): return 1 + 3
        elif(b == "Z"):  return 2 + 6
    elif(a == "B") :
        if(b == "X"): return 1 + 0
        elif(b == "Y"): return 2 + 3
        elif(b == "Z"):  return 3 + 6
    elif(a == "C") :
        if(b == "X"): return 2 + 0
        elif(b == "Y"): return 3 + 3
        elif(b == "Z"):  return 1 + 6

instructions = open(file_path, "r")
score = 0
for i in instructions :
    split = i.split()
    score += get_score(split[0], split[1])
 
print(score)
instructions.close();   