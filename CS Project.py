
from tkinter import *
import csv
filename=open("Salary Details.csv","r",newline='')
file=csv.reader(filename)
Head=['Employee ID','Employee Name','DOB','DOJ','AGE','Gender','Company Name','Branch','Department','Designation','Bank Name','IFSC Code','PAN No','Aadhar no','Basic pay','DA','HRA','SA','Gross Salary','Yearly Gross','Graduvity','No.of working days','No.of leaves taken','EPF','TDS','Leave Deduction','Other Deduction','Total Deduction','Net Pay']

nested_cont=[]
for i in file:
    nested_cont.append(i)

main=Tk()
a=StringVar()
b=StringVar()

Admin=[["Vijay","1234vija"],["Shantha","1234shan"],["SMAditya","1234adit"],["Keerthi","1234keer"]]

def submit():
    UN,PW=a.get(),b.get()
    if [UN,PW] in Admin:
        global Login
        Login=True
        main.destroy()
    else:
        Login=False
        Label(main,text="Login Unsucessful")    .grid(row=4)
    
    

def options():
    global opt
    opt=Tk()
    B2=Button(opt,text="ViewEMP",width=10,command=select_tk)         .grid(row=1,column=1)
    B3=Button(opt,text="Add",width=10,command=add_tk)                .grid(row=2,column=1)
    B4=Button(opt,text="Modify",width=10,command=modify_tk)          .grid(row=3,column=1)
    B5=Button(opt,text="Delete",width=10,command=delete_tk)          .grid(row=4,column=1)
    B6=Button(opt,text="Clearall",width=10,command=clearall_tk)      .grid(row=5,column=1)
    B7=Button(opt,text="Print ",width=10,command=print_tk)           .grid(row=6,column=1)
    opt.mainloop()


#View Selected
def select_tk():
    opt.destroy()
    sel=Tk()
    a=StringVar()
    def submit():
        empID=a.get()
        out=select(empID)
        Label(sel,text=out,justify='left')        .grid(row=4)
        def opts():
            sel.destroy()
            options()
            sel.mainloop
        B=Button(sel,text="Back",width=7,command=opts)      .grid(row=5,column=0)
        
        
    Label(sel,text="Enter Employee ID:")        .grid(row=0,column=0)
    E1=Entry(sel,textvariable=a)                .grid(row=0,column=1)
    Button(sel,text="Enter",command=submit)     .grid(row=2)
    

def select(empID):
    filename.seek(0)
    L=[]
    for i in file:
        L.append(i[0])
        if i[0]==empID:
            s=''
            for j in range(len(Head)):
                for k in range(len(i)):
                    if j==k:
                        s+=Head[j]+" :   "+i[k]+"\n"
            return s
    if empID not in L:
        return "No such employee ID !"
    
def delete_tk():
    opt.destroy()
    global sel
    sel=Tk()
    a=StringVar()
    def submit():
        empID=a.get()
        delete(empID)
        def opts():
            sel.destroy()
            options()
            sel.mainloop
        B=Button(sel,text="Back",width=7,command=opts)      .grid(row=5,column=0)
    Label(sel,text="Enter Employee ID:")        .grid(row=0,column=0)
    E1=Entry(sel,textvariable=a)                .grid(row=0,column=1)
    Button(sel,text="Enter",command=submit)     .grid(row=2)
    
    

def delete(empID):
    filename.seek(0)
    found=False
    L=[]
    for i in file:
        if i[0]==empID:
            found=True
        else:
            L.append(i)
    
    if found==False:
        Label(sel,text="No such employee ID !").grid(row=3)
    else:
        file1=open("Salary Details.csv","w+",newline='')
        writer=csv.writer(file1)
        writer.writerows(L)
        Label(sel,text="Record Deleted Sucessfully").grid(row=3)

    
def clearall_tk():
    filename.seek(0)
    opt.destroy()
    global sel
    sel=Tk()
    a=StringVar()
    def submit():
        c=a.get()
        if c=="Yes":
            L=[]
            file1=open("Salary Details.csv","w",newline='')
            writer=csv.writer(file1)
            writer.writerows(L)
            Label(sel,text="Clear Successful")                 .grid(row=4)
        else:
            Label(sel,text="Declined")                     .grid(row=4)
        def opts():
            sel.destroy()
            options()
            sel.mainloop
        B=Button(sel,text="Back",width=7,command=opts)      .grid(row=5,column=0)
    Label(sel,text="Confirm Clear Database (Yes/No) :")        .grid(row=0,column=0)
    E1=Entry(sel,textvariable=a)                               .grid(row=0,column=1)
    Button(sel,text="Enter",command=submit)                    .grid(row=2)
    sel.mainloop()

def add_tk():
    opt.destroy()

    global sel
    sel=Tk()
    

    a1=StringVar()
    b1=StringVar()
    c1=StringVar()
    d1=StringVar()
    e1=StringVar()
    f1=StringVar()
    g1=StringVar()
    h1=StringVar()
    i1=StringVar()
    j1=StringVar()
    k1=StringVar()
    l1=StringVar()
    m1=StringVar()
    n1=StringVar()
    o1=StringVar()
    p1=StringVar()
    q1=StringVar()
    r1=StringVar()
    s1=StringVar()
    t1=StringVar()

    def submit():
        d={'Employee ID':a1.get(),'Employee Name':b1.get(),'DOB':q1.get(),'DOJ':r1.get(),'AGE':s1.get(),'Gender':t1.get(),'Company Name':c1.get(),'Branch':d1.get(),'Department':e1.get(),'Designation':f1.get(),'Bank Name':g1.get(),'IFSC Code':h1.get(),'PAN No':i1.get(),'Aadhar no':j1.get(),'Basic pay':k1.get(),'DA':l1.get(),'SA':m1.get(),'No.of working days':n1.get(),'No.of leaves taken':o1.get(),'Other Deduction':p1.get()}
        add(d)

    Label(sel,text="Enter Employee ID").grid(row=0,column=0)
    E1=Entry(sel,textvariable=a1).grid(row=0,column=1)

    Label(sel,text="Enter Employee Name").grid(row=1,column=0)
    E1=Entry(sel,textvariable=b1).grid(row=1,column=1)

    Label(sel,text="DOB").grid(row=2,column=0)
    E1=Entry(sel,textvariable=q1).grid(row=2,column=1)

    Label(sel,text="DOJ").grid(row=3,column=0)
    E1=Entry(sel,textvariable=r1).grid(row=3,column=1)

    Label(sel,text="AGE").grid(row=4,column=0)
    E1=Entry(sel,textvariable=s1).grid(row=4,column=1)

    Label(sel,text="Gender").grid(row=5,column=0)
    E1=Entry(sel,textvariable=t1).grid(row=5,column=1)

    Label(sel,text="Enter Company Name").grid(row=6,column=0)
    E1=Entry(sel,textvariable=c1).grid(row=6,column=1)

    Label(sel,text="Enter Branch").grid(row=7,column=0)
    E1=Entry(sel,textvariable=d1).grid(row=7,column=1)

    Label(sel,text="Enter Department").grid(row=8,column=0)
    E1=Entry(sel,textvariable=e1).grid(row=8,column=1)

    Label(sel,text="Enter Designation").grid(row=9,column=0)
    E1=Entry(sel,textvariable=f1).grid(row=9,column=1)

    Label(sel,text="Enter Bank Name").grid(row=10,column=0)
    E1=Entry(sel,textvariable=g1).grid(row=10,column=1)

    Label(sel,text="Enter IFSC Code").grid(row=11,column=0)
    E1=Entry(sel,textvariable=h1).grid(row=11,column=1)

    Label(sel,text="Enter PAN No").grid(row=12,column=0)
    E1=Entry(sel,textvariable=i1).grid(row=12,column=1)

    Label(sel,text="Enter Aadhar no").grid(row=13,column=0)
    E1=Entry(sel,textvariable=j1).grid(row=13,column=1)

    Label(sel,text="Enter Basic pay").grid(row=14,column=0)
    E1=Entry(sel,textvariable=k1).grid(row=14,column=1)

    Label(sel,text="Enter DA").grid(row=15,column=0)
    E1=Entry(sel,textvariable=l1).grid(row=15,column=1)

    Label(sel,text="Enter SA").grid(row=16,column=0)
    E1=Entry(sel,textvariable=m1).grid(row=16,column=1)

    Label(sel,text="Enter No.of working days").grid(row=17,column=0)
    E1=Entry(sel,textvariable=n1).grid(row=17,column=1)

    Label(sel,text="Enter No.of leaves taken").grid(row=18,column=0)
    E1=Entry(sel,textvariable=o1).grid(row=18,column=1)

    Label(sel,text="Enter Other Deduction").grid(row=19,column=0)
    E1=Entry(sel,textvariable=p1).grid(row=19,column=1)

    Button(sel,text="Confirm",command=submit).grid(row=21,column=0)
    
    def opts():
        sel.destroy()
        options()
        sel.mainloop
    B=Button(sel,text="Back",width=7,command=opts)      .grid(row=23,column=0)

def add(d):
    print(d)
    calc_dbm(d)
    cond=d['Employee ID'].isdigit() and len(d['Employee ID'])==8 and len(d['Employee Name']) <= 20 and d['IFSC Code'][:4].isalpha() and d['IFSC Code'][4:].isdigit() and len(d['IFSC Code'])==10 and d['PAN No'].isalnum() and len(d['PAN No'])==10 and d['Aadhar no'].isdigit() and len(d['Aadhar no'])==12 and int(d['No.of working days'])<=31 and int(d['No.of leaves taken'])<=31
    if cond:
        add_rec=[]
        for i in Head:
            for j in d:
                if i==j:
                    add_rec.append(d[i])
        nested_cont.append(add_rec)
        filename1=open("Salary Details.csv","w",newline='')
        cr=csv.writer(filename1)
        cr.writerows(nested_cont)
        Label(sel,text="Record added successfully !").grid(row=22,column=0)
    else:
        Label(sel,text="Detail Conditions not satisfied").grid(row=22,column=0)

def modify_tk():
    opt.destroy()
    filename.seek(0)
    

    def submit():
        global empID
        empID=a.get()
        input.destroy()

    input=Tk()
    a=StringVar()
    Label(input,text="Enter Employee ID:")        .grid(row=0,column=0)
    E1=Entry(input,textvariable=a)                .grid(row=0,column=1)
    Button(input,text="Enter",command=submit)     .grid(row=2)
    input.mainloop()

    global d
    d={}
    for i in nested_cont:
        if i[0] == empID:
            rec=i
    for j in range(len(Head)):
        for k in range(len(rec)):
            if j==k:
                d[Head[j]]=rec[k]
    ind=nested_cont.index(rec)

    global sel
    sel=Tk()


    a1=StringVar()
    b1=StringVar()
    c1=StringVar()
    d1=StringVar()
    e1=StringVar()
    f1=StringVar()
    g1=StringVar()
    h1=StringVar()
    i1=StringVar()
    j1=StringVar()
    k1=StringVar()
    l1=StringVar()
    m1=StringVar()
    n1=StringVar()
    o1=StringVar()
    p1=StringVar()
    q1=StringVar()
    r1=StringVar()

    def modify():
        d={'Employee ID':EmpID,'Employee Name':EmpName,'DOB':a1.get(),'DOJ':b1.get(),'AGE':q1.get(),'Gender':r1.get(),'Company Name':c1.get(),'Branch':d1.get(),'Department':e1.get(),'Designation':f1.get(),'Bank Name':g1.get(),'IFSC Code':h1.get(),'PAN No':i1.get(),'Aadhar no':j1.get(),'Basic pay':k1.get(),'DA':l1.get(),'SA':m1.get(),'No.of working days':n1.get(),'No.of leaves taken':o1.get(),'Other Deduction':p1.get()}
        cond=d['Employee ID'].isdigit() and len(d['Employee ID'])==8 and len(d['Employee Name']) <= 20 and d['IFSC Code'][:4].isalpha() and d['IFSC Code'][4:].isdigit() and len(d['IFSC Code'])==10 and d['PAN No'].isalnum() and len(d['PAN No'])==10 and d['Aadhar no'].isdigit() and len(d['Aadhar no'])==12 and float(d['No.of working days'])<31 and float(d['No.of leaves taken'])<=31
        if cond:
            calc_dbm(d)
            L=[]
            for i in Head:
                for j in d:
                    if i==j:
                        L.append(d[i])
            nested_cont[ind]=L
            print(L)

            filename1=open("Salary Details.csv","w+",newline='')
            cr=csv.writer(filename1)
            cr.writerows(nested_cont)          
            filename1.close()
            Label(sel,text="Record modified successfully !").grid(row=22,column=0)

            def opts():
                sel.destroy()
                options()
                sel.mainloop

            B=Button(sel,text="Back",width=7,command=opts)      .grid(row=23,column=0) 

        else:
            Label(sel,text="Detail Conditions not satisfied").grid(row=22,column=0)

    Label(sel,text="Employee ID").grid(row=0,column=0)
    Label(sel,text=d['Employee ID']).grid(row=0,column=1)
    EmpID=d['Employee ID']

    Label(sel,text="Employee Name").grid(row=1,column=0)
    Label(sel,text=d['Employee Name']).grid(row=1,column=1)
    EmpName=d['Employee Name']

    Label(sel,text="DOB").grid(row=2,column=0)
    E1=Entry(sel,textvariable=a1)
    E1.insert(0,d['DOB']);E1.grid(row=2,column=1)

    Label(sel,text="DOJ").grid(row=3,column=0)
    E1=Entry(sel,textvariable=b1)
    E1.insert(0,d['DOJ']);E1.grid(row=3,column=1)

    Label(sel,text="AGE").grid(row=4,column=0)
    E1=Entry(sel,textvariable=q1)
    E1.insert(0,d['AGE']);E1.grid(row=4,column=1)

    Label(sel,text="Gender").grid(row=5,column=0)
    E1=Entry(sel,textvariable=r1)
    E1.insert(0,d['Gender']);E1.grid(row=5,column=1)

    Label(sel,text="Company Name").grid(row=6,column=0)
    E1=Entry(sel,textvariable=c1)
    E1.insert(0,d['Company Name']);E1.grid(row=6,column=1)

    Label(sel,text="Branch").grid(row=7,column=0)
    E1=Entry(sel,textvariable=d1)
    E1.insert(0,d['Branch']);E1.grid(row=7,column=1)

    Label(sel,text="Department").grid(row=8,column=0)
    E1=Entry(sel,textvariable=e1)
    E1.insert(0,d['Department']);E1.grid(row=8,column=1)

    Label(sel,text="Designation").grid(row=9,column=0)
    E1=Entry(sel,textvariable=f1)
    E1.insert(0,d['Designation']);E1.grid(row=9,column=1)

    Label(sel,text="Bank Name").grid(row=10,column=0)
    E1=Entry(sel,textvariable=g1)
    E1.insert(0,d['Bank Name']);E1.grid(row=10,column=1)

    Label(sel,text="IFSC Code").grid(row=11,column=0)
    E1=Entry(sel,textvariable=h1)
    E1.insert(0,d['IFSC Code']);E1.grid(row=11,column=1)

    Label(sel,text="PAN No").grid(row=12,column=0)
    E1=Entry(sel,textvariable=i1)
    E1.insert(0,d['PAN No']);E1.grid(row=12,column=1)

    Label(sel,text="Aadhar no").grid(row=13,column=0)
    E1=Entry(sel,textvariable=j1)
    E1.insert(0,d['Aadhar no']);E1.grid(row=13,column=1)

    Label(sel,text="Basic pay").grid(row=14,column=0)
    E1=Entry(sel,textvariable=k1)
    E1.insert(0,d['Basic pay']);E1.grid(row=14,column=1)

    Label(sel,text="DA").grid(row=15,column=0)
    E1=Entry(sel,textvariable=l1)
    E1.insert(0,d['DA']);E1.grid(row=15,column=1)

    Label(sel,text="SA").grid(row=16,column=0)
    E1=Entry(sel,textvariable=m1)
    E1.insert(0,d['SA']);E1.grid(row=16,column=1)

    Label(sel,text="No.of working days").grid(row=17,column=0)
    E1=Entry(sel,textvariable=n1)
    E1.insert(0,d['No.of working days']);E1.grid(row=17,column=1)

    Label(sel,text="No.of leaves taken").grid(row=18,column=0)
    E1=Entry(sel,textvariable=o1)
    E1.insert(0,d['No.of leaves taken']);E1.grid(row=18,column=1)

    Label(sel,text="Other Deduction").grid(row=19,column=0)
    E1=Entry(sel,textvariable=p1)
    E1.insert(0,d['Other Deduction']);E1.grid(row=19,column=1)

    Button(sel,text="Confirm",command=modify).grid(row=21,column=0) 

def print_tk():
    opt.destroy()
    d={}
    def submit():
        global empID
        empID=a.get()
        for i in nested_cont:
            if i[0] == empID:
                rec=i
        else:
            Label(input,text="No Such Employee")        .grid(row=3,column=0)

        for j in range(len(Head)):
            for k in range(len(rec)):
                if j==k:
                    d[Head[j]]=rec[k]
        input.destroy()

    input=Tk()
    a=StringVar()
    Label(input,text="Enter Employee ID:")        .grid(row=0,column=0)
    E1=Entry(input,textvariable=a)                .grid(row=0,column=1)
    Button(input,text="Enter",command=submit)     .grid(row=2)
    
    input.mainloop()

    sel=Tk()

    Label(sel,text="BLISS PvT Ltd").grid(row=0,column=2)

    Label(sel,text="Employee ID:",justify='left').grid(row=2,column=0)
    Label(sel,text=d['Employee ID'],justify='left').grid(row=2,column=1)


    Label(sel,text="Employee Name:",justify='left').grid(row=3,column=0)
    Label(sel,text=d['Employee Name'],justify='left').grid(row=3,column=1)


    Label(sel,text="Company Name:",justify='left').grid(row=4,column=0)
    Label(sel,text=d['Company Name'],justify='left').grid(row=4,column=1)


    Label(sel,text="Branch:",justify='left').grid(row=5,column=0)
    Label(sel,text=d['Branch'],justify='left').grid(row=5,column=1)


    Label(sel,text="Department:",justify='left').grid(row=6,column=0)
    Label(sel,text=d['Department'],justify='left').grid(row=6,column=1)


    Label(sel,text="Designation:",justify='left').grid(row=2,column=3)
    Label(sel,text=d['Designation'],justify='left').grid(row=2,column=4)


    Label(sel,text="Bank Name:",justify='left').grid(row=3,column=3)
    Label(sel,text=d['Bank Name'],justify='left').grid(row=3,column=4)


    Label(sel,text="IFSC Code:",justify='left').grid(row=4,column=3)
    Label(sel,text=d['IFSC Code'],justify='left').grid(row=4,column=4)


    Label(sel,text="PAN No:",justify='left').grid(row=5,column=3)
    Label(sel,text=d['PAN No'],justify='left').grid(row=5,column=4)


    Label(sel,text="Aadhar no:",justify='left').grid(row=6,column=3)
    Label(sel,text=d['Aadhar no'],justify='left').grid(row=6,column=4)


    Label(sel,text="Basic pay").grid(row=8,column=0)
    Label(sel,text=d['Basic pay']).grid(row=9,column=0)


    Label(sel,text="DA").grid(row=8,column=1)
    Label(sel,text=d['DA']).grid(row=9,column=1)


    Label(sel,text="HRA").grid(row=8,column=2)
    Label(sel,text=d['HRA']).grid(row=9,column=2)


    Label(sel,text="SA").grid(row=8,column=3)
    Label(sel,text=d['SA']).grid(row=9,column=3)


    Label(sel,text="Gross Salary",justify='left').grid(row=11,column=0)
    Label(sel,text=d['Gross Salary'],justify='left').grid(row=11,column=1)


    Label(sel,text="Graduvity",justify='left').grid(row=12,column=0)
    Label(sel,text=d['Graduvity'],justify='left').grid(row=12,column=1)


    Label(sel,text="No.of leaves taken",justify='left').grid(row=13,column=0)
    Label(sel,text=d['No.of leaves taken'],justify='left').grid(row=13,column=1)


    Label(sel,text="EPF",justify='left').grid(row=14,column=0)
    Label(sel,text=d['EPF'],justify='left').grid(row=14,column=1)

    
    Label(sel,text="TDS",justify='left').grid(row=11,column=3)
    Label(sel,text=d['TDS'],justify='left').grid(row=11,column=4)


    Label(sel,text="Leave Deduction",justify='left').grid(row=12,column=3)
    Label(sel,text=d['Leave Deduction'],justify='left').grid(row=12,column=4)


    Label(sel,text="Other Deduction",justify='left').grid(row=13,column=3)
    Label(sel,text=d['Other Deduction'],justify='left').grid(row=13,column=4)


    Label(sel,text="Total Deduction",justify='left').grid(row=14,column=3)
    Label(sel,text=d['Total Deduction'],justify='left').grid(row=14,column=4)


    Label(sel,text="Net Pay",justify='left').grid(row=16,column=0)
    Label(sel,text=d['Net Pay'],justify='left').grid(row=16,column=1)

    def opts():
        sel.destroy()
        options()
        sel.mainloop
    B=Button(sel,text="Back",width=7,command=opts)      .grid(row=17,column=0)

def calc_dbm(d):
    d['HRA']=float(int(d['Basic pay'])*0.4)
    d['SA']=d['SA']
    d['Gross Salary']=float(int(d['Basic pay'])+int(d['DA'])+int(d['HRA'])+int(d['SA']))
    d['Yearly Gross']=float(int(d['Gross Salary'])*12)
    d['Graduvity']=float(int(d['Basic pay'])*0.083)
    d['No.of working days']=d['No.of working days']
    d['No.of leaves taken']=d['No.of leaves taken']
    d['EPF']=float(int(d['Basic pay'])*0.07)
    d['TDS']=calc_TDS(float(d['Yearly Gross']))
    d['Leave Deduction']=float(float(d['Gross Salary'])*float(d['No.of leaves taken'])/float(d['No.of working days']))
    d['Other Deduction']=d['Other Deduction']    
    d['Total Deduction']=float(int(d['EPF'])+int(d['TDS'])+int(d['Leave Deduction'])+int(d['Other Deduction']))
    d['Net Pay']=float(int(d['Gross Salary'])-int(d['Total Deduction']))
    updrec=d.values()
    return list(updrec)

def calc_TDS(x):
    TDS=0
    if x<=250000:
        TDS+=0
    elif x<=500000:
        TDS+=x*0.05
    elif x<=750000:
        TDS+=12500+((x-500000)*0.1)
    elif x<=1000000:
        TDS+=37500+((x-750000)*0.15)
    elif x<=1250000:
        TDS+=75000+((x-1000000)*0.2)
    elif x<=1500000:
        TDS+=125000+((x-1250000)*0.25)
    else:
        TDS+=187500+((x-1500000)*0.3)
    return TDS/12

Label(main,text="Username:")                .grid(row=0,column=0)
E1=Entry(main,textvariable=a)               .grid(row=0,column=1)
Label(main,text="Password:")                .grid(row=1,column=0)
E2=Entry(main,show="*",textvariable=b)      .grid(row=1,column=1)
Button(main,text="Enter",command=submit)    .grid(row=2)
main.mainloop()

f=True
while f:
    if Login:
        f=False
        options()

filename.close()



