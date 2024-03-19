
import random as rd
import string
import hashlib



ALPHABET = string.ascii_uppercase

alphabet = string.ascii_lowercase

al123 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

al_ = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "<", ">", "-", "_", ".", ",", ":", ";", "(", ")", "?", "'", '"', "/"]

combined_al = [ALPHABET, alphabet, al123, al_]
all_al = [i for sublist in combined_al for i in sublist]


sh_log = []
sh_log2 = []
sh_pas = []
sh_pas2 =[]


def sCea(log, pas):
    X = 0
    g = rd.randint(1, 83)
    g = int(g)
    Y = rd.randint(100, 10000000)
    log2 = ""
    log4 = ""
    i = 0
    j = 0
    while len(log) != i:
        while log[i] != all_al[j]:
            j += 1
            if j == len(all_al):
                print("Ошибка")
                break
        sh_log.append(((j+g) % 85) + 10)
        j = 0
        i += 1

    i = 0
    j = 0

    while len(pas) != i:
        while pas[i] != all_al[j]:
            j += 1
            if j == len(all_al):
                print("Ошибка")
                break
        sh_pas.append(((j+g) % 85) + 10)
        j = 0
        i += 1

    i = 0
    #print(log)
    #print(sh_log)
    log2 = str(sh_log)

    i = 0
    log4 = str(sh_pas)


    #print(sh_log)
    #print(log2)
    hash_object = hashlib.md5(log2.encode())
    ha = hash_object.hexdigest()

    hash_object2 = hashlib.md5(log4.encode())
    ha2 = hash_object2.hexdigest()
    #print(ha)
    return ha, ha2, Y, g

def dCea(log, pas, g):
    log3 = ""
    log5 = ""
    i = 0
    j = 0
    while len(pas) != i:
        while pas[i] != all_al[j]:
            j += 1
            if j == len(all_al):
                print("Ошибка")
                break
        sh_pas2.append(((j+g) % 85) + 10)
        j = 0
        i += 1

    i = 0
    j = 0

    while len(log) != i:
        while log[i] != all_al[j]:
            j += 1
            if j == len(all_al):
                print("Ошибка")
                break
        sh_log2.append(((j+g) % 85) + 10)
        j = 0
        i += 1
    #print(sh_log2)
    log3 = str(sh_log2)


    log5 = str(sh_pas2)


    hash_object1 = hashlib.md5(log3.encode())
    ha1 = hash_object1.hexdigest()
    hash_object3 = hashlib.md5(log5.encode())
    ha3 = hash_object3.hexdigest()
    #print(ha1)
    return ha1, ha3
