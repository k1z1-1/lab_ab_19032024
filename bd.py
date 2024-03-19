


import sqlite3


def base(role, log, pas, k, k2):
    db = sqlite3.connect("date.db")

    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS users3 (role INTEGER, login TEXT, pas TEXT, k INTEGER, k2 INTEGER)""")

    db.commit()
    role1 = role
    log1 = log
    pas1 = pas
    k1 = k
    k3 = k2
    print(role1, log1, pas1, k1, k3)

    sql.execute(f"INSERT INTO users3 VALUES (?, ?, ?, ?, ?)", (role1, log1, pas1, k1, k3))
    db.commit()




def base2(kod):
    db = sqlite3.connect("date.db")

    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS users3 (role INTEGER, login TEXT, pas TEXT, k INTEGER, k2 INTEGER)""")

    db.commit()
    kod1 = kod
    sql.execute(f"SELECT k FROM users3 WHERE k = '{kod1}'")
    if sql.fetchone() is None:
        db.commit()

        return 2, 1
    else:

        return 1, kod1


def base3(kod):
    db = sqlite3.connect("date.db")

    sql = db.cursor()

    sql.execute("""CREATE TABLE IF NOT EXISTS users3 (role INTEGER, login TEXT, pas TEXT, k INTEGER, k2 INTEGER)""")

    db.commit()
    kod1 = kod
    sql.execute(f"SELECT role FROM users3 WHERE k = '{kod1}'")
    role = sql.fetchone()[0]
    sql.execute(f"SELECT login FROM users3 WHERE k = '{kod1}'")
    login = sql.fetchone()[0]
    sql.execute(f"SELECT pas FROM users3 WHERE k = '{kod1}'")
    pas = sql.fetchone()[0]
    sql.execute(f"SELECT k FROM users3 WHERE k = '{kod1}'")
    k = sql.fetchone()[0]
    sql.execute(f"SELECT k2 FROM users3 WHERE k = '{kod1}'")
    k1 = sql.fetchone()[0]
    db.commit()

    return role, login, pas, k, k1