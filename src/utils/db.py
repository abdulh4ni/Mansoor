import sqlite3
from os.path import isfile

BUILD_PATH = "./db/build.sql"
DB_PATH = "./db/db.sqlite3"

cxn = sqlite3.connect(DB_PATH)
cur = cxn.cursor()


def build():
    if isfile(BUILD_PATH):
        with open(BUILD_PATH, 'r') as script:
            sqlexec = script.read()

        cur.execute(sqlexec)
    else:
        print("BUILD_PATH not found")
        return


def commit():
    cxn.commit()


def close():
    cxn.close()


def execute(sql, *values):
    cur.execute(sql, tuple(values))


def record(sql, *values):
    cur.execute(sql, tuple(values))
    return cur.fetchone()