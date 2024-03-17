from lib import *

clear()

emp = {}

confirm = pbluei("start appending? ",color=CYAN,t=0.01).strip().lower() in ['y','yes','yeag','ya','yah']

def is_q(inp):
    return inp == "q"

if confirm:
    while(True):
        clear()
        name = pgreeni("name(q): ",color=CYAN,t=0.03).strip().title()        
        if is_q(name):
            break
        age = pgreeni("age(q): ",color=CYAN,t=0.03).strip()
        if is_q(age):
            break
        sal = pgreeni("salary(q): $", color=CYAN,t=0.03).strip()
        if is_q(sal):
            break

        emp = {"name":name,"age":age,"salary":sal}
        insert_data(list(emp.values()))

confirm = pbluei("show data? ",t=0.01,color=CYAN).strip().lower() in ['y','yes','yeah','ya','yah']

if confirm:
    clear()
    emps = fetch_data(list=True)
    emps.sort(key=lambda x: len(x['name']))
    emps_2 = fetch_data()
    mout = f"{len(emps)}"
    mname = max(len(name) for name in emps_2['name'])
    mage = max(len(age) for age in emps_2['age'])
    msal = max(len(f"{int(sal):,}") for sal in emps_2['salary'])

    mn,ma,ms = "", "", ""
    for _ in range(mname):
        mn += " "
    for _ in range(mage):
        ma += " "
    for _ in range(msal):
        ms += " "

    for i,emp in enumerate(emps):
        out = f"{i+1}"
        out,mout = equalize(out,mout)
        name = f"{emp['name']}"
        age = f"{emp['age']}"
        sal = f"{int(emp['salary']):,}"
        name,mn = equalize(name,mn)
        age,ma = equalize(age,ma)
        sal,ms = equalize(sal,ms)
        pyellow(f"\033[1;93m{out}: \033[0;96m{name}, {BLUE}{age}, {GREEN}${sal}",t=0.0005)
        