import sqlite3 as lite
import sys
import os.path
import datetime


def writeEntry(entry,link):
    dbfile = 'entries.db'
    if  not os.path.exists(dbfile):
        con = lite.connect(dbfile)
        with con:
            cur = con.cursor()    
            cur.execute("CREATE table entries(entry TEXT, link TEXT, datetime timestamp)")
        con = ''

    con = lite.connect(dbfile)
    with con:
        cur = con.cursor()
        cur.execute('insert into entries values(?,?,?)', (entry, link, datetime.datetime.now()))
        # cur.execute('insert into entries values(?,?,?,?)', (23, 't1', 'http://google.com', datetime.datetime.now()))


    with con:
        cur = con.cursor()    
        cur.execute("SELECT * FROM entries")
        rows = cur.fetchall()
        for row in rows:
            print row


if __name__ == '__main__':
    writeEntry('222','http://ww.sqlite.org/')