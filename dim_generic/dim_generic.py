import sqlite3 as sq

dim=sq.connect('dims12.db')
cur=dim.cursor()

def generic(n):
    cur.execute("select generic_name from t_drug_generic where `_rowid_`={}".format(n))
    g=cur.fetchall()
    if g == None:
        return "None"
    else:
        return g.replace("\n"," ")
def
