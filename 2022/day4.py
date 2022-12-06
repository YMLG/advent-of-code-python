from os import path
import re
file_path = path.realpath("2022/resources/input4.txt")
#===================*============================
lignes = open(file_path, "r")
total = 0
for ligne in lignes:
    assignments = [int(n) for n in re.split(",|-",ligne)]
    if (assignments[0] <= assignments[2] and assignments[1] >= assignments[3]) or (assignments[2] <= assignments[0] and assignments[3] >= assignments[1])  :
        total += 1
print(total)
lignes.close();   
#===================* *============================
lignes = open(file_path, "r")
total = 0
for ligne in lignes:
    assignments = [int(n) for n in re.split(",|-",ligne)]
    if (assignments[0] <= assignments[2] and assignments[2] <= assignments[1]) or (assignments[2] <= assignments[0] and assignments[0] <= assignments[3]) or (assignments[0] <= assignments[3] and assignments[3] <= assignments[1]) or  (assignments[2] <= assignments[1] and assignments[1] <= assignments[3]):
        total += 1
print(total)
lignes.close();   