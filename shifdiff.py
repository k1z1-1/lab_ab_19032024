
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


def sDif(log, pas):
    X = 0
    g = rd.randint(100, 150)
    with open('Простые числа.txt') as f:
        for strok, line in enumerate(f, 1):
            if strok == g:
                break
    g = int(line)
    k = rd.randint(100, 150)
    with open('Простые числа.txt') as f:
        for strok, line in enumerate(f, 1):
            if strok == k:
                break
    k = int(line)
    p = rd.randint(100, 150)
    with open('Простые числа.txt') as f:
        for strok, line in enumerate(f, 1):
            if strok == p:
                break
    p = int(line)

    log2 = ""
    log4 = ""
    fl = 0
    while fl == 0:
        q = rd.randint(60, 100)
        with open('Простые числа.txt') as f:
            for strok, line in enumerate(f, 1):
                if strok == q:
                    break
        q = int(line)
        if int(q) < p - 1:
            X = int(q)
            fl = 1



    Y = pow(g, X, p)
    Y = pow(Y, k)



    i = 0
    j = 0
    while len(log) != i:
        while log[i] != all_al[j]:
            j += 1
            if j == len(all_al):
                print("Ошибка")
                break
        sh_log.append(j + 10)
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
        sh_pas.append(j + 10)
        j = 0
        i += 1

    i = 0
    #print(log)
    #print(sh_log)
    for i in range(len(sh_log)):
        sh_log[i] = pow(sh_log[i] * Y, 1, p)
        if (sh_log[i] < 100000000) and (sh_log[i] >= 10000000):
            sh_log[i] = str(sh_log[i])
        elif (sh_log[i] < 10000000) and (sh_log[i] >= 1000000):
            sh_log[i] = "0" + str(sh_log[i])
        elif (sh_log[i] < 1000000) and (sh_log[i] >= 100000):
            sh_log[i] = "00" + str(sh_log[i])
        elif (sh_log[i] < 100000) and (sh_log[i] >= 10000):
            sh_log[i] = "000" + str(sh_log[i])
        elif (sh_log[i] < 10000) and (sh_log[i] >= 1000):
            sh_log[i] = "0000" + str(sh_log[i])
        log2 = log2 + sh_log[i]

    i = 0
    for i in range(len(sh_pas)):
        sh_pas[i] = pow(sh_pas[i] * Y, 1, p)
        if (sh_pas[i] < 100000000) and (sh_pas[i] >= 10000000):
            sh_pas[i] = str(sh_pas[i])
        elif (sh_pas[i] < 10000000) and (sh_pas[i] >= 1000000):
            sh_pas[i] = "0" + str(sh_pas[i])
        elif (sh_pas[i] < 1000000) and (sh_pas[i] >= 100000):
            sh_pas[i] = "00" + str(sh_pas[i])
        elif (sh_pas[i] < 100000) and (sh_pas[i] >= 10000):
            sh_pas[i] = "000" + str(sh_pas[i])
        elif (sh_pas[i] < 10000) and (sh_pas[i] >= 1000):
            sh_pas[i] = "0000" + str(sh_pas[i])
        log4 = log4 + sh_pas[i]


    #print(sh_log)
    #print(log2)
    hash_object = hashlib.md5(log2.encode())
    ha = hash_object.hexdigest()

    hash_object2 = hashlib.md5(log4.encode())
    ha2 = hash_object2.hexdigest()
    #print(ha)
    return ha, ha2, Y, p

def dDif(log, pas, Y, p):
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
        sh_pas2.append(j + 10)
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
        sh_log2.append(j + 10)
        j = 0
        i += 1
    #print(sh_log2)
    for i in range(len(sh_log2)):
        sh_log2[i] = pow(sh_log2[i] * Y, 1, p)
        if (sh_log2[i] < 100000000) and (sh_log2[i] >= 10000000):
            sh_log2[i] = str(sh_log2[i])
        elif (sh_log2[i] < 10000000) and (sh_log2[i] >= 1000000):
            sh_log2[i] = "0" + str(sh_log2[i])
        elif (sh_log2[i] < 1000000) and (sh_log2[i] >= 100000):
            sh_log2[i] = "00" + str(sh_log2[i])
        elif (sh_log2[i] < 100000) and (sh_log2[i] >= 10000):
            sh_log2[i] = "000" + str(sh_log2[i])
        elif (sh_log2[i] < 10000) and (sh_log2[i] >= 1000):
            sh_log2[i] = "0000" + str(sh_log2[i])
        log3 = log3 + sh_log2[i]


    for i in range(len(sh_pas2)):
        sh_pas2[i] = pow(sh_pas2[i] * Y, 1, p)
        if (sh_pas2[i] < 100000000) and (sh_pas2[i] >= 10000000):
            sh_pas2[i] = str(sh_pas2[i])
        elif (sh_pas2[i] < 10000000) and (sh_pas2[i] >= 1000000):
            sh_pas2[i] = "0" + str(sh_pas2[i])
        elif (sh_pas2[i] < 1000000) and (sh_pas2[i] >= 100000):
            sh_pas2[i] = "00" + str(sh_pas2[i])
        elif (sh_pas2[i] < 100000) and (sh_pas2[i] >= 10000):
            sh_pas2[i] = "000" + str(sh_pas2[i])
        elif (sh_pas2[i] < 10000) and (sh_pas2[i] >= 1000):
            sh_pas2[i] = "0000" + str(sh_pas2[i])
        log5 = log5 + sh_pas2[i]


    hash_object1 = hashlib.md5(log3.encode())
    ha1 = hash_object1.hexdigest()
    hash_object3 = hashlib.md5(log5.encode())
    ha3 = hash_object3.hexdigest()
    #print(ha1)
    return ha1, ha3
