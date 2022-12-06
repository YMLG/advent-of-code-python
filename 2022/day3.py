from os import path
file_path = path.realpath("2022/resources/input3.txt")

def get_score(l):
    low = l.lower()
    score = ord(low) - 96
    if(low != l) : score += 26
    return score

#===================*============================
lignes = open(file_path, "r")
total = 0
for ligne in lignes :
    a = ligne[:int(len(ligne)/2)]
    b = ligne[int(len(ligne)/2):]
    for lettre in a:
        if lettre in b : 
            total += get_score(lettre)
            break
print(total)
lignes.close();   
#===================* *============================
lignes = open(file_path, "r")
total = 0
ligne = lignes.readline()
while ligne != "":
    l1 = lignes.readline()
    l2 = lignes.readline()
    for lettre in ligne:
        if lettre in l1 and  lettre in l2: 
            total += get_score(lettre)
            break
    ligne  = lignes.readline()
print(total)
lignes.close();   