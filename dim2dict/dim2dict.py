import sqlite3 as lite

conn = lite.connect('dims12.db')
cur = conn.cursor()


def brand_name(n):
    cur.execute("select brand_name from t_drug_brand where `_rowid_` like {}".format(n))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " ")
def form(n):
    cur.execute("select form from t_drug_brand where `_rowid_` like {}".format(n))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " ")
def strength(n):
    cur.execute("select strength from t_drug_brand where `_rowid_` like {}".format(n))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " ")
def company(n):
    cur.execute("select company_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    #print(g.__len__()==0)
    if g.__len__()==0:
        return ""
    else:
        cur.execute("select company_name from t_company_name where company_id={}".format(g[0][0]))
        a = cur.fetchall()
        if a == []:
            return exec(n+1)
        else:

            b=a[0][0]
            if b == None:
                return "None"
            else:
                return b.replace("\n", " ")


#print(brand_name(1)[0][0])
def generic_name(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select generic_name from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    #print("look here")
    #print(a==[])
    if a == []:
        return exec(n+1)
    else:

        b=a[0][0]
        if b == None:
            return "None"
        else:
            return b.replace("\n", " ")
def indication(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select indication from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " ")
#print(indication(1))[0][0]
def dose(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select dose from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " ")
def contra_indication(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select contra_indication from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " ")
def side_effect(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select side_effect from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " "  )
def precaution(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select precaution from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " ")
def pregnancy_category(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select pregnancy_category_id from t_drug_generic where generic_id={}".format(g[0][0]))
    p = cur.fetchall()
    if p == []:
        return ""
    else:
        cur.execute("select pregnancy_name from t_pregnancy_category where pregnancy_id={}".format(p[0][0]))
        a = cur.fetchall()
        if a == []:
            return exec(n+1)
        else:
            b=a[0][0]
            if b == None:
                return "None"
            else:
                return b.replace("\n", " ")
def mode_of_action(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select mode_of_action from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " ")
def interaction(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select interaction from t_drug_generic where generic_id={}".format(g[0][0]))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " ")
def therapeutic_id(n):
    cur.execute("select generic_id from t_drug_brand where `_rowid_`={}".format(n))
    g=cur.fetchall()
    cur.execute("select therapitic_id from t_therapitic_generic where generic_id={}".format(g[0][0]))
    t=cur.fetchall()

    if t == []:
        return exec(n+1)
    else:
        cur.execute("select therapitic_name from t_therapitic where therapitic_id={}".format(t[0][0]))
        a = cur.fetchall()
        if a == []:
            return exec(n+1)
        else:

            b=a[0][0]
            if b == None:
                return "None"
            else:
                return b.replace("\n", " ")


def packsize(n):
    cur.execute("select packsize from t_drug_brand where `_rowid_` like {}".format(n))
    a = cur.fetchall()
    b=a[0][0]
    if b == None:
        return "None"
    else:
        return b.replace("\n", " ")

def printall(n):
    #print(n)
    print(brand_name(n),end =" ")
    print(form(n),end =" ")
    print(strength(n),end =" ")
    print(packsize(n),end =" ")
    print(company(n),end ="\t")
    print("<t>n : "+generic_name(n),end ="<n>")
    print("<t>Indications : "+indication(n),end ="<n>")
    print("<t>Doses and administration : "+dose(n),end ="<n>")
    print("<t>Contara-indications : "+contra_indication(n),end ="<n>")
    print("<t>Side effects : "+side_effect(n),end ="<n>")
    print("<t>Precaution : "+precaution(n),end ="<n>")
    print("<t>Pregnancy category : "+pregnancy_category(n),end ="<n>")
    print("<t>Mode of action : "+mode_of_action(n),end ="<n>")
    print("<t>Interaction : "+interaction(n),end ="<n>")
    print("<t>Therapeutic class : "+therapeutic_id(n),end ="\n")
def exec(n):
    while n<17589:
        printall(n)
        n += 1
#print(generic_name(1045))
#exec()
#exec(1)