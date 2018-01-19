import sqlite3 as lite

conn = lite.connect('dims12.db')
cur = conn.cursor()


def brand_name(n):
    cur.execute("select brand_name from t_drug_brand where `_rowid_` like {}".format(n))
    a = cur.fetchall()
    b=a[0][0]
    c=b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
    return c.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")

#print(brand_name(1)[0][0])
def generic_name(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select generic_name from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    c=b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
    return c.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
def indication(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select indication from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    c=b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
    return c.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
#print(indication(1))[0][0]
def dose(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select dose from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    c=b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
    return c.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
def contra_indication(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select contra_indication from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
def side_effect(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select side_effect from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
def precaution(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select precaution from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
def pregnancy_category(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select pregnancy_category_id from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    c=b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
    return c.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
def mode_of_action(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select mode_of_action from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    c=b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
    return c.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
def interaction(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select interaction from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
def therapeutic_id(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select therapitic_id from t_therapitic_generic where generic_id={}".format(g[0][0]))
    t=cur.fetchall()
    cur.execute("select therapitic_name from t_therapitic where therapitic_id={}".format(t[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    c=b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
    return c.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")
def packsize(n):
    cur.execute("select packsize from t_drug_brand where `_rowid_` like {}".format(n))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t").replace("\n","\n\t")

def printall(n):
    #print(n)
    print(brand_name(n))
    print("\tn : "+generic_name(n))
    print("\tIndications : "+indication(n))
    print("\tDoses and administration : "+dose(n))
    print("\tContara-indications : "+contra_indication(n))
    print("\tSide effects : "+side_effect(n))
    print("\tPrecaution : "+precaution(n))
    print("\tPregnancy category : "+pregnancy_category(n))
    print("\tMode of action : "+mode_of_action(n))
    print("\tInteraction : "+interaction(n))
    print("\tTherapeutic class : "+therapeutic_id(n))
    print("\tPacksize : "+packsize(n))
n = 1
while n<1045:
    printall(n)
    n = n+1
n=1048
while n<17586:
    printall(n)
    n=n+1