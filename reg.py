import string

ALPHABET = string.ascii_uppercase

alphabet = string.ascii_lowercase

al123 = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

al_ = ["~", "!", "@", "#", "$", "%", "^", "&", "*", "<", ">", "-", "_", ".", ",", ":", ";", "(", ")", "?", "'", '"', "/"]


combined_al = [ALPHABET, alphabet, al123, al_]
all_al = [i for sublist in combined_al for i in sublist]



def rg(log, pas):
    n = 0
    i = 0
    f = 0
    j1 = 0
    j2 = 0
    j3 = 0
    j4 = 0
    fj1 = 0
    fj2 = 0
    fj3 = 0
    fj4 = 0
    f_log = 0
    if (len(pas) > 5) and (len(pas) < 13):
        n += 1
        while f == 0:

            while pas[i] != ALPHABET[j1]:
                j1 += 1
                if j1 == len(ALPHABET) - 1:
                    j1 = 90
                    break
            if j1 != 90:
                fj1 += 1
            j1 = 0
            while pas[i] != alphabet[j2]:
                j2 += 1
                if j2 == len(alphabet) - 1:
                    j2 = 900
                    break
            if j2 != 900:
                fj2 += 1
            j2 = 0
            while pas[i] != al123[j3]:
                j3 += 1
                if j3 == len(al123) - 1:
                    j3 = 9000
                    break
            if j3 != 9000:
                fj3 += 1
            j3 = 0
            while pas[i] != al_[j4]:
                j4 += 1
                if j4 == len(al_) - 1:
                    j4 = 90000
                    break
            if j4 != 90000:
                fj4 += 1
            j4 = 0
            i += 1
            if i == len(pas):
                f = 1
    elif len(pas) < 6:
        print("Маленький пароль")

    elif len(pas) > 12:
        print("Большой пароль")
    print(fj1, fj2, fj3, fj4)
    i = 0
    if len(log) > 8:
            while log[i] !="@":
                i += 1
                if i == len(log) - 1:
                    break
            if log[i] == "@":
                if len(log) - i == 10:
                    if log[-9:] == "gmail.com":
                        f_log = 1
                    #elif log[-9:] == "yandex.ru":
                    #    f_log = 1
                elif len(log) - i == 8:
                    if log[-7:] == "mail.ru":
                        f_log = 1

    if (fj1> 0) and (fj2> 0) and (fj3> 0) and (fj4> 0) and (f_log> 0):
        print("ура")

    if f_log == 0:
        return 1
    elif fj1 == 0:
        return 2
    elif fj2 == 0:
        return 3
    elif fj3 == 0:
        return 4
    elif fj4 == 0:
        return 5
    else:
        return 6