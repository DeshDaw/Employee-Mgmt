#Manually Create a Database "job" in my sql

def base(): #to make sure its connected and to check if table is created or not
    a = "SHOW TABLES;"
    cursor.execute(a)
    results = cursor.fetchall()
    results_list = [item[0] for item in results] #convert into string

#to check whether table emp is present in the system before proceeding
#if the table is'nt present, it'll create a table automatically
    
    if not "emp" in results_list:
        print("Creating table emp...")
        b="create table emp(empno int(20) auto_increment primary key, name varchar(50), age int(3), marital varchar(10))"
        cursor.execute(b)
        con.commit()
        print("Table structure EMP created successfully\n")
    
    else:
        print("Table EMP already exists\n")
        
#to check whether table info is present in the system before proceeding
#if the table is'nt present, it'll create a table automatically
    
    if not "info" in results_list:
        print("Creating table info...")
        b="create table info(empno int(20) auto_increment primary key, experience int(3), behavior varchar(20), salary decimal(30,2), start_cont date, end_cont date, check(start_cont<end_cont))"
        cursor.execute(b)
        con.commit()
        print("Table structure INFO created successfully\n")
    
    else:
        print("Table INFO already exists\n")


#-------------------------------------------


def add(): #to insert value
    while True:
        global salary
        num=7
        empno=num + 1
        name=input("Enter employee's name:")
        age=int(input("Enter employee's age:"))
        if age>70:
            print("Unfortunatly, the entered age is over over the required age group\nYou will be exited out of this form")
            break
        if age<17:
            print("Unfortunatly, the entered age is over under the required age group\nYou will be exited out of this form")
            break
        experience=int(input("Enter employee's experience in years:"))
        marital=input("Enter employee's name ('M' for married / 'S' for single):") #marital status
        if marital.lower()=="m": #changes "m" to "Married" (for more understanding)
            marital="Married"
        if marital.lower()=="s": #changes "s" to "Single" (for more understanding)
            marital="Single"
        behavior=input("Enter employee's behavior status ('G' for good / 'B' for bad):") #behavior status
        if behavior.lower()=="g": 
            behavior="On time"
        if behavior.lower()=="b":
            behavior="Late   "
        start_cont=input("Enter start of contract date in YYYY/MM/DD:")
        end_cont=input("Enter end of contract date in YYYY/MM/DD:")
        if end_cont<start_cont:
            print("Entered contract date is not applicable./n Please make sure the contract end date is after the contract start date")
            start_cont=input("Enter start of contract date in YYYY/MM/DD:")
            end_cont=input("Enter end of contract date in YYYY/MM/DD:")
        salary=float(input("Enter the employee's salary: "))
        print("")
        if marital=="Married":
            salary=salary+salary*0.2
            print("Salary is increased by 20% due to marital status")
        if behavior=="On time":
            salary=salary+salary*0.1
            print("Salary is increased by 10% due to on time attendance")
        if behavior=="Late":
            salary=salary-salary*0.1
            print("Salary is decreased by 10% due to late time attendance")
        if experience>5:
            salary=salary+salary*0.1
            print("Salary is increased by 10% because experience is more than 5 years ")
            
        c="insert into emp (name, age, marital) values('{}', {}, '{}')".format(name.title(), age, marital)
        cursor.execute(c)
        con.commit()
        d="insert into info (experience, behavior, salary, start_cont, end_cont) values({}, '{}', {}, '{}', '{}')".format(experience, behavior, salary, start_cont, end_cont)
        cursor.execute(d)
        con.commit()
        print("\nValue entered!")
        break

#-------------------------------------------

import csv
def csvadd():
    f=open("emp.csv","a",newline="")
    n=int(input("How many records needed: "))
    lines=[]
    for i in range(n):
        global salary
        no=int(input("Enter the number:"))
        name=input("Enter employee's name:")
        age=int(input("Enter employee's age:"))
        if age>70:
            print("Unfortunatly, the entered age is over over the required age group\nYou will be exited out of this form")
            break
        if age<17:
            print("Unfortunatly, the entered age is over under the required age group\nYou will be exited out of this form")
            break
        experience=int(input("Enter employee's experience in years:"))
        marital=input("Enter employee's name ('M' for married / 'S' for single):") #marital status
        if marital.lower()=="m": #changes "m" to "Married" (for more understanding)
            marital="Married"
        if marital.lower()=="s": #changes "s" to "Single" (for more understanding)
            marital="Single"
        behavior=input("Enter employee's behavior status ('G' for good / 'B' for bad):") #behavior status
        if behavior.lower()=="g": 
            behavior="On time"
        if behavior.lower()=="b":
            behavior="Late"
        salary=float(input("Enter the employee's salary: "))
        print("")
        if marital=="Married":
            salary=salary+salary*0.2
            print("Salary is increased by 20% due to marital status")
        if behavior=="On time":
            salary=salary+salary*0.1
            print("Salary is increased by 10% due to on time attendance")
        if behavior=="Late":
            salary=salary-salary*0.1
            print("Salary is decreased by 10% due to late time attendance")
        if experience>5:
            salary=salary+salary*0.1
            print("Salary is increased by 10% because experience is more than 5 years ")
        data=[no,name,age,marital,behavior,salary]
        lines.append(data)
    d=csv.writer(f)
    d.writerows(lines)
    f.close()

#-------------------------------------------

import pickle
def binaryadd():
    f1=open("emp.dat","ab")
    n=int(input("Enter total no of records :"))
    record=[]
    for i in range(n):
        global salary
        no=int(input("Enter the number:"))
        name=input("Enter employee's name:")
        age=int(input("Enter employee's age:"))
        if age>70:
            print("Unfortunatly, the entered age is over over the required age group\nYou will be exited out of this form")
            break
        if age<17:
            print("Unfortunatly, the entered age is over under the required age group\nYou will be exited out of this form")
            break
        experience=int(input("Enter employee's experience in years:"))
        marital=input("Enter employee's name ('M' for married / 'S' for single):") #marital status
        if marital.lower()=="m": #changes "m" to "Married" (for more understanding)
            marital="Married"
        if marital.lower()=="s": #changes "s" to "Single" (for more understanding)
            marital="Single"
        behavior=input("Enter employee's behavior status ('G' for good / 'B' for bad):") #behavior status
        if behavior.lower()=="g": 
            behavior="On time"
        if behavior.lower()=="b":
            behavior="Late"
        salary=float(input("Enter the employee's salary: "))
        print("")
        if marital=="Married":
            salary=salary+salary*0.2
            print("Salary is increased by 20% due to marital status")
        if behavior=="On time":
            salary=salary+salary*0.1
            print("Salary is increased by 10% due to on time attendance")
        if behavior=="Late":
            salary=salary-salary*0.1
            print("Salary is decreased by 10% due to late time attendance")
        if experience>5:
            salary=salary+salary*0.1
            print("Salary is increased by 10% because experience is more than 5 years ")
        data=[no,name,age,marital,behavior,salary]
        record.append(data)
    pickle.dump(record,f1)
    f1.close()

#-------------------------------------------


def search(): #to search in emp table
    
    print("Search employee data by")
    print("1. Number")
    print("2. Name")
    print("3. Marital status")
    print("4. Behaivor")
    print("5. Salary")
    print("")
    ch=int(input("Enter your choice:"))
    
    if ch==1: #to search employee using employee number
        no=int(input("Enter the Employee's number you would like to get details on:"))
        d="select emp.empno, emp.name, emp.age, emp.marital, info.experience, info.behavior, info.salary, info.start_cont, info.end_cont from emp inner join info on emp.empno=info.empno where info.empno={};".format(no)
        cursor.execute(d)
        rs=cursor.fetchall()
        print("-"*125)
        print("empno \t| name        \t | age  \t| marital \t | experience  | behavior  | salary \t  | start_cont   \t | end_cont \t | ")
        print("-"*125)
        for i in rs:
            for j in i:
                print(j, end="\t | ")
            print()
        print("-"*125)
    
    elif ch==2:
        name=input("Enter the Employee's name you would like to get details on:")
        d="select emp.empno, emp.name, emp.age, emp.marital, info.experience, info.behavior, info.salary, info.start_cont, info.end_cont from emp inner join info on emp.empno=info.empno where emp.name='{}'".format(name)
        cursor.execute(d)
        rs=cursor.fetchall()
        print("-"*125)
        print("empno \t| name        \t | age  \t| marital \t | experience  | behavior  | salary \t  | start_cont   \t | end_cont \t | ")
        print("-"*125)
        for i in rs:
            for j in i:
                print(j, end="\t | ")
            print()
        print("-"*125)
    
    elif ch==3:
        ma=input("Enter the Employee's marital status you would like to get details on (M/S):")
        if ma.lower()=="m": 
            ma="Married"
        if ma.lower()=="s": 
            ma="Single"
        d="select emp.empno, emp.name, emp.age, emp.marital, info.experience, info.behavior, info.salary, info.start_cont, info.end_cont from emp inner join info on emp.empno=info.empno where emp.marital='{}'".format(ma)
        cursor.execute(d)
        rs=cursor.fetchall()
        print("-"*125)
        print("empno \t| name        \t | age  \t| marital \t | experience  | behavior  | salary \t  | start_cont   \t | end_cont \t | ")
        print("-"*125)
        for i in rs:
            for j in i:
                print(j, end="\t | ")
            print()
        print("-"*125)
    
    elif ch==4:
        bh=input("Enter the Employee's behavior you would like to get details on(G/B):")
        if bh.lower()=="g": 
            bh="On time"
        if bh.lower()=="b":
            bh="Late"
        d="select emp.empno, emp.name, emp.age, emp.marital, info.experience, info.behavior, info.salary, info.start_cont, info.end_cont from emp inner join info on emp.empno=info.empno where info.behavior='{}'".format(bh)
        cursor.execute(d)
        rs=cursor.fetchall()
        print("-"*125)
        print("empno \t| name        \t | age  \t| marital \t | experience  | behavior  | salary \t  | start_cont   \t | end_cont \t | ")
        print("-"*125)
        for i in rs:
            for j in i:
                print(j, end="\t | ")
            print()
        print("-"*125)
        
    elif ch==5:
        sl=input("Enter the Employee's salary you would like to get details on(salary above the entered value will be displayed):")
        d="select emp.empno, emp.name, emp.age, emp.marital, info.experience, info.behavior, info.salary, info.start_cont, info.end_cont from emp inner join info on emp.empno=info.empno where info.salary>={}".format(sl)
        cursor.execute(d)
        rs=cursor.fetchall()
        print("-"*125)
        print("empno \t| name        \t | age  \t| marital \t | experience  | behavior  | salary \t  | start_cont   \t | end_cont \t | ")
        print("-"*125)
        for i in rs:
            for j in i:
                print(j, end="\t | ")
            print()
        print("-"*125)
    
#-------------------------------------------

def csvsearch(): #[no,name,age,marital,behavior,salary]
    print("Search employee data by")
    print("1. Number")
    print("2. Name")
    print("3. Marital status")
    print("4. Behaivor")
    print("5. Salary")
    print("")
    ch=int(input("Enter your choice:"))
    
    if ch==1: #to search employee using employee number
        no=input("Enter the Employee's number you would like to get details on:")
        f=open("emp.csv","r")
        d=csv.reader(f)
        for i in d:
            if i[0]==no:
                print(i)
                break
        else:
            print("not found")
        f.close()

    elif ch==2:
        name=input("Enter the Employee's name you would like to get details on:")
        f=open("emp.csv","r")
        d=csv.reader(f)
        for i in d:
            if i[1]==name:
                print(i)
                break
        else:
            print("not found")
        f.close()
    
    elif ch==3:
        ma=input("Enter the Employee's marital status you would like to get details on (M/S):")
        f=open("emp.csv","r")
        d=csv.reader(f)
        for i in d:
            if i[3]==ma:
                print(i)
        else:
            print("not found")
        f.close()
    
    elif ch==4:
        bh=input("Enter the Employee's behavior you would like to get details on(G/B):")
        f=open("emp.csv","r")
        d=csv.reader(f)
        for i in d:
            if i[4]==bh:
                print(i)
        else:
            print("not found")
        f.close()
        
    elif ch==5:
        sl=input("Enter the Employee's salary you would like to get details on(salary above the entered value will be displayed):")
        f=open("emp.csv","r")
        d=csv.reader(f)
        for i in d:
            if i[5]==sl:
                print(i)
        else:
            print("not found")
        f.close()

#-------------------------------------------

def binarysearch(): #[no,name,age,marital,behavior,salary]
    print("Search employee data by")
    print("1. Number")
    print("2. Name")
    print("3. Marital status")
    print("4. Behaivor")
    print("5. Salary")
    print("")
    ch=int(input("Enter your choice:"))
    
    if ch==1: #to search employee using employee number
        no=int(input("Enter the Employee's number you would like to get details on:"))
        f2=open("emp.dat","rb")
        d=pickle.load(f2)
        for i in d:
            if i[0]==no:
                print("Details of the employee is :",i)
                break
        else:
            print("Not Found.")
        f2.close()

    elif ch==2:
        name=input("Enter the Employee's name you would like to get details on:")
        f2=open("emp.dat","rb")
        d=pickle.load(f2)
        for i in d:
            if i[1]==name:
                print("Details of the employee is :",)
                break
        else:
            print("Not Found.")
        f2.close()
    
    elif ch==3:
        ma=input("Enter the Employee's marital status you would like to get details on (M/S):")
        f2=open("emp.dat","rb")
        d=pickle.load(f2)
        for i in d:
            if i[3]==ma:
                print("Details of the employee is :",i)
        else:
            print("Not Found.")
        f2.close()

    elif ch==4:
        bh=input("Enter the Employee's behavior you would like to get details on(G/B):")
        f2=open("emp.dat","rb")
        d=pickle.load(f2)
        for i in d:
            if i[4]==bh:
                print("Details of the employee is :",i)
        else:
            print("Not Found.")
        f2.close()
        
    elif ch==5:
        sl=input("Enter the Employee's salary you would like to get details on(salary above the entered value will be displayed):")
        f=open("emp.csv","r")
        d=csv.reader(f)
        for i in d:
            if i[5]==sl:
                print(i)
        else:
            print("not found")
        f.close()

#-------------------------------------------


def update(): #to update any values
    no=int(input("Enter the Employee's number you would like to update:"))
    
    print("What would you like to update\n")
    print("1. Name")
    print("2. Age")
    print("3. experience")
    print("4. Salary")
    print("5. Start of contract")
    print("6. End of contract")
    
    ch=int(input("Enter your choice:"))
    print("")
    
    if ch==1:
        nm=input("Enter the new name:")
        d=" update emp set name='{}' where empno={};".format(nm.title(), no)
        cursor.execute(d)
        con.commit()
        print("\nValue updated!")
    
    elif ch==2:
        nm=input("Enter the new age:")
        d=" update emp set age={} where empno={};".format(nm, no)
        cursor.execute(d)
        con.commit()
        print("\nValue updated!")
        
    elif ch==3:
        nm=input("Enter the new experience:")
        d=" update info set experience={} where empno={};".format(nm, no)
        cursor.execute(d)
        con.commit()
        print("\nValue updated!")
        
    elif ch==4:
        nm=input("Enter the new salary:")
        d="update info set salary={} where empno={};".format(nm, no)
        cursor.execute(d)
        con.commit()
        print("\nValue updated!")
        
    elif ch==5:
        nm=input("Enter the new Start contract date (YYYY/MM/DD):")
        d="update info set start_cont='{}' where empno={};".format(nm, no)
        cursor.execute(d)
        con.commit()
        print("\nValue updated!")
        
    elif ch==6:
        nm=input("Enter the new End contract date (YYYY/MM/DD):")
        d="update info set end_cont='{}' where empno={};".format(nm, no)
        cursor.execute(d)
        con.commit()
        print("\nValue updated!")

#-------------------------------------------


def delete(): #to delete any entry in emp table
    
    no=int(input("Enter the Employee's number you would like to delete:"))
    d="delete from emp where empno={}".format(no)
    cursor.execute(d)
    con.commit()
    c="delete from info where empno={}".format(no)
    cursor.execute(c)
    con.commit()
    print("\nValue deleted!")


#-------------------------------------------


def conf_view(): #to view all the entered data
    
    d="select emp.empno, emp.name, emp.age, emp.marital, info.experience, info.behavior, info.salary, info.start_cont, info.end_cont from emp inner join info on emp.empno=info.empno;"
    
    cursor.execute(d)
    rs=cursor.fetchall()
    print("-"*125)
    print("empno \t| name        \t | age  \t| marital \t | experience  | behavior  | salary \t  | start_cont   \t | end_cont \t | ")
    print("-"*125)
    for i in rs:
        for j in i:
            print(j, end="\t | ")
        print()
    print("-"*125)


#-------------------------------------------


def csvconf_view(): #to view all the entered data
    
    f=open("emp.csv","r")
    
    d=csv.reader(f)
    for i in d:
        print(i)
    f.close()

    
#-------------------------------------------


def binaryconf_view(): #to view all the entered data
    
    
    f=open("emp.dat","rb")
    
    d=pickle.load(f)
    for i in d:
        print(i)
    f.close()

    
#-------------------------------------------



def nonconf_view(): #to view all the entered data but for employees (less detailed data)
       
    d="select emp.empno, emp.name, emp.age, info.salary from emp inner join info on emp.empno=info.empno;"
    cursor.execute(d)
    rs=cursor.fetchall()
    print("-"*50)
    print("empno \t| name   \t  | age  \t| salary \t  |")
    print("-"*50)
    for i in rs:
        for j in i:
            print(j, end="\t | ")
        print()
    print("-"*50)



#-------------------------------------------



def csvnonconf_view(): #to view all the entered data but for employees (less detailed data)
       
    f=open("emp.csv","r")
    
    d=csv.reader(f)
    for i in d:
        print("[",i[0],",'",i[1],"',",i[2],",",i[5],"]")
    f.close()



#-------------------------------------------



def binarynonconf_view(): #to view all the entered data but for employees (less detailed data)
       
    f=open("emp.dat","rb")
    
    d=pickle.load(f)
    for i in d:
        print("[",i[0],",'",i[1],"',",i[2],",",i[5],"]")
    f.close()



#*******************************************************


def sort():
    print("Count/sort employees by: \n")
    print("1. Age")
    print("2. experience")
    print("3. Marital status")
    print("4. Behaivor")
    
    ch=int(input("Enter your choice:"))
    
    if ch==1:
        a="select age, count(*) as number from emp group by age;"
        cursor.execute(a)
        rs=cursor.fetchall()
        print("-"*27)
        print("age \t| number  |")
        print("-"*27)
        for i in rs:
            for j in i:
                print(j, end="\t | ")
            print()
        print("-"*27)
        
    if ch==2:
        a="select experience, count(*) as number from info group by experience;"
        cursor.execute(a)
        rs=cursor.fetchall()
        print("-"*27)
        print("experience| number  |")
        print("-"*27)
        for i in rs:
            for j in i:
                print(j, end="\t | ")
            print()
        print("-"*27)
    
    if ch==3:
        a="select marital, count(*) as number from emp group by marital;"
        cursor.execute(a)
        rs=cursor.fetchall()
        print("-"*27)
        print("marital \t| number  |")
        print("-"*27)
        for i in rs:
            for j in i:
                print(j, end="\t | ")
            print()
        print("-"*27)
        
    if ch==4:
        a="select behavior, count(*) as number from info group by behavior;"
        cursor.execute(a)
        rs=cursor.fetchall()
        print("-"*27)
        print("behavior \t| number  |")
        print("-"*27)
        for i in rs:
            for j in i:
                print(j, end="\t | ")
            print()
        print("-"*27)
    

#*******************************************************


#MAIN CODE

print("Please wait...  \n")

import mysql.connector as m
pswd=input("enter the password: ")
con=m.connect(host='localhost', user="root", password=pswd, database="Job")
cursor=con.cursor()

if con.is_connected():
    base()
    
    while True:
        
        print("1. Add an employee")
        print("2. Search an employee")
        print("3. Update data of an employee")
        print("4. Delete an employee")
        print("5. View all data (for employees; Confidential)")
        print("6. View all data (for employees; Non-confidential)")
        print("7. Count/sort data from sql")
        print("8. Exit \n")
        
        ch=int(input("Enter your choice:"))
        print("")
        
        if ch==1:
            print("1. To create CSV file")
            print("2. To create Binary file")
            print("3. To create sql table")

            op=int(input("Enter the option:"))
            if op==1:
                csvadd()
            elif op==2:
                binaryadd()
            elif op==3:
                add()
        elif ch==2:
            print("1. To search in CSV file")
            print("2. To search in Binary file")
            print("3. To search in sql table")

            op=int(input("Enter the option:"))
            if op==1:
                csvsearch()
            elif op==2:
                binarysearch()
            elif op==3:
                search()
                
        elif ch==3:
            update()
            
        elif ch==4:
            delete()
            
        elif ch==5:
            
            print("1. To show all the info in CSV file")
            print("2. To show all the info in Binary file")
            print("3. To show all the info in sql table")

            op=int(input("Enter the option:"))
            if op==1:
                csvconf_view()
            elif op==2:
                binaryconf_view()
            elif op==3:
                conf_view()
                
        elif ch==6:
            
            print("1. To show all the info in CSV file")
            print("2. To show all the info in Binary file")
            print("3. To show all the info in sql table")

            op=int(input("Enter the option:"))
            if op==1:
                csvnonconf_view()
            elif op==2:
                binarynonconf_view()
            elif op==3:
                nonconf_view()
                
        elif ch==7:
            sort()
            
        
        ch=input("\nDo you want to return to the menu (y/n):")
        if ch.lower()=="n":
            break
        
        elif ch==8:
            print("You've successfully exited")
            break
        
else:
    print("Sorry :(  Not able to connect, reconnect")
    
