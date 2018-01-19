import sqlite3 as lite

db = lite.connect('dims12.db')
cur = db.cursor()

def pregnancy_category(p):
    cur.execute("select pregnancy_name from t_pregnancy_category where pregnancy_id={}".format(p[0][0]))
    a = cur.fetchall()
    if a == []:
        return ""
    else:
        b=a[0][0]
        if b == None:
            return "None"
        else:
            return b.replace("\n", " ")

def generic_name(n):
    cur.execute("select generic_name from t_drug_generic where _rowid_={}".format(n))
    g = cur.fetchall()[0][0]
    if g==None:
        return array(n+1)
    else:
        return g

def brand_names(n):
    cur.execute("select generic_id,generic_name,indication,dose,contra_indication,side_effect,precaution,pregnancy_category_id,mode_of_action,interaction from t_drug_generic where _rowid_ = {}".format(n))
    gi=cur.fetchall()
    #print(gi)
    if gi[0][1]==None:
       name =""
    else:
        name=gi[0][1]
    if gi[0][2]==None:
        ind=""
    else:
        ind=gi[0][2]
    if gi[0][3]==None:
        dose=""
    else:
        dose=gi[0][3]
    if gi[0][4]==None:
        cind=""
    else:
        cind=gi[0][4]
    if gi[0][5]==None:
        se=""
    else:
        se=gi[0][5]

    if gi[0][6]==None:
        pct=""
    else:
        pct=gi[0][6]
    if gi[0][7]==None:
        preg=""
    else:
        preg=pregnancy_category(gi[0][7])

    if gi[0][8]==None:
        moa=""
    else:
        if gi==[]:
            moa=""
        else:
            moa=gi[0][8]
    if gi[0][9]==None:
        interaction=""
    else:
        interaction=gi[0][9]
    generic_info="<t>Indication: "+""+ind+"<n><n>"+"Dose: "+""+dose+"<n><n>"+"Contra-indication: "+""+cind+"<n><n>""Side effects: "+""+se+"<n><n>"+"Precaution: "+""+pct+"<n><n>"+"Mode of action: "+""+str(moa)+"<n><n>"+"Pregnancy category: "+preg+"<n><n>"+"Interaction: "+""+ interaction
    if gi==None:
        return ""
    else:

        cur.execute("select company_id,brand_name,form,strength,packsize,price from t_drug_brand where generic_id={} order by company_id * 1".format(gi[0][0]))
        g = cur.fetchall()
        #print(g)
        brands=""
        r=""
        #print(g)
        for i in g:
            #print(i)
            if i[0]==0:
                company=""
            else:
                #company =dim.company(i[0]).replace(" Pharmaceuticals Ltd.","").replace(" Limited","")
                cur.execute("select company_name from t_company_name where company_id={}".format(i[0]))
                c = cur.fetchall()
                if c==None:
                    company=""
                else:
                    if c==[]:
                        company = ""
                    else:
                        company=c[0][0]
            if i[1]==None:
                brand=""
            else:
                brand = i[1]
            if i[2]==None:
                form=""
            else:
                form = i[2]
            if i[3]==None:
                strength=""
            else:
                strength = i[3]
            if i[4]==None:
                pack=""
            else:
                pack = i[4]
            if i[5]==None:
                price=""
            else:
                price= i[5]
            brand_info=("<n>"+str(company)+"<t>"+brand+" "+form+" "+strength+" "+pack+" "+price+" BDT").replace("Dr Tablet", "TAB dr")\
            .replace("Tablet","TAB dr").replace("Capsule","CAP")
            brands=brands+"<n><t>"+brand_info

        r=r+"<n>"+brands.replace(" Pharmaceuticals Ltd.","").replace(" Limited","").replace(" Pharmaceutical Ltd","").replace(" Laboratories","").replace(" limited","")
        s = name+"\t"+r+"<n>"+generic_info
        return s.replace("\n","<n>")
def array(n):
    array =[]

    while n<1435:
        array.append(generic_name(n))
        n=n+1
    return array
def dict(n):
    dict={}
    key = generic_name(n)
    while n<1436:
        dict.key = []

#print(dict(1))
#print(brand_names(23))
def execute(n):
    while n<1436:
        #print(n)
        print(brand_names(n))
        n=n+1
execute(1)