


import smtplib
import random as rd


def snd(mail):
    sender = "mikola.cocicola@gmail.com"
    password = "fqqpalxqdjwfgatn"
    g = rd.randint(1000, 9999)
    print(g)
    msg = str(g)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, mail, msg)
    return g


def snd_kod(mail, Y):
    sender = "mikola.cocicola@gmail.com"
    password = "fqqpalxqdjwfgatn"
    msg = str(Y)

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, mail, msg)
    return Y

