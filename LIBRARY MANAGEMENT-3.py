#this programme is a library manangement software where the staff members can save and access the information of the students that have issued books(updated, menus=5)
import mysql.connector as a
import datetime
import pyttsx3
engine=pyttsx3.init()
engine.say("This program is related with library management")
engine.runAndWait()
con=a.connect(host="localhost",user="root",passwd="")
mycursor=con.cursor(buffered=True)
try:
    mycursor.execute("create database project")
except:
    pass
mycursor.execute("use project")
try:
    mycursor.execute("create table books(bnumber varchar(100) not null,bname varchar(100) not null,bAuthor varchar(100) not null,tbook varchar(50) not null,sub varchar(200) not null)")
except:
    pass
try:
    mycursor.execute("create table issue(registration_no varchar(200) not null,name varchar(100) not null,contact varchar(10) not null,bookname varchar(100),bnumber varchar(100),date_issue varchar(200))")
except:
    pass
def addbook():
    bk=input("enter book name:")
    mycursor.execute("select count(*) from books")
    for j in mycursor:
        w=j[0]
    mycursor.execute("select * from books order by bnumber desc LIMIT 1")
    au=input("enter name of the Author/Writter/institute:")
    t=input("total books copies available:")
    s=input("enter subject:")
    if w==0:
        k=1
    else:
        for i in mycursor:
            k=int(i[0])+1
    print("your book's number is",str(k))
    sql='INSERT INTO books values("%s","%s","%s","%s","%s")'%(str(k),bk,au,t,s)
    mycursor.execute(sql)
    con.commit()
    engine.say("data entered successfully")
    engine.runAndWait()
    print("data entered successfully")
    print("................................................")
    main()
def issueb():
    n=input("Enter student's name:")
    bco=input("Enter book's number:")
    mycursor.execute("select * from books")
    for u in mycursor:
        if bco==u[0] and int(u[3])!=0:
            o=u[1]
            a=int(u[3])-1
            wer="update books set tbook='%s' where bnumber='%s'"%(str(a),bco)
            mycursor.execute(wer)
            while True:
                nob=input("Enter your Contact no.:")
                if len(nob)!=10:
                    print("INVALID PHONE NO.")
                    continue
                else:
                    break
            date_bookissued=datetime.datetime.now()
            week=datetime.timedelta(days=7)
            date_submission=date_bookissued+week
            q=str(date_bookissued)
            print("date of issuing=",date_bookissued)
            print("date of submission",date_submission)
            mycursor.execute("select count(*) from issue")
            for j in mycursor:
                w=j[0]
            mycursor.execute("select * from issue order by registration_no desc LIMIT 1")
            if w==0:
                r=1
            else:
                for k in mycursor:
                    r=int(k[0])+1
            print("your registration number is:",str(r))
            a='insert into issue values("%s","%s","%s","%s","%s","%s")'%(r,n,nob,u[1],u[0],q[0:10])
            mycursor.execute(a)
            con.commit()
            print(".........................................")
            print("Book '"+o+"' has been issued to:",n)
            engine.say("data entered successfully")
            engine.runAndWait()
        elif int(u[3])==0:
            print("THE BOOK IS CURRENTLY OUT OF STOCK")
            engine.say("THE BOOK IS CURRENTLY OUT OF STOCK")
            engine.runAndWait()
    main()
def submit():
    r=input("enter registeration number:")
    mycursor.execute("select * from issue")
    filza=mycursor.fetchall()
    for k in filza:
        if k[0]==r:
            print(k)
            l=input("The following student has returned the book(y/n):")
            if l=="y":
                d="delete from issue where registration_no='%s'"%(r)
                mycursor.execute(d)
                p=k[4]
                n=k[1]
                mycursor.execute("select * from books")
                for y in mycursor:
                    if p==y[0]:
                        m=str(int(y[3])+1)
                sql="update books set tbook='%s' where bnumber='%s'"%(m,p)
                mycursor.execute(sql)
                print(".........................................")
                print("book submitted from:",n)
                con.commit()
                engine.say("Book submitted")
                engine.runAndWait()
            else:
                engine.say("OK!,Come back later if the student submits the book")
                engine.runAndWait()
                print("OK!,Come back later if the student submits the book")
    main()
def available():
    e=input("enter book number:")
    mycursor.execute("select * from books")
    for t in mycursor:
        if t[0]==e:
            s=input("how many books of "+t[1]+" available now:")
            sql="update books set tbook='%s' where bnumber='%s'"%(s,e)
            mycursor.execute(sql)
            print("total number of book",t[1],"updated to:",s)
    con.commit()
    engine.say("data updated")
    engine.runAndWait()
    main()
def book():
    ac=input("enter book number:")
    a="delete from books where bnumber='%s'"%(ac)
    mycursor.execute(a)
    con.commit()
    engine.say("SUCCESSFULLY DELETED")
    engine.runAndWait()
    print("SUCCESSFULLY DELETED")
    main()
def dispbook():
    a="select * from books"
    mycursor.execute(a)
    myresult=mycursor.fetchall()
    engine.say("here are the following results")
    engine.runAndWait()
    for i in myresult:
        print("book number:",i[0])
        print("book name:",i[1])
        print("Author/Writter/Institute:",i[2])
        print("Total books in stock:",i[3])
        print("Subject:",i[4])
        print("...........................")
    main()
def issuedbook():
    a="select * from issue"
    mycursor.execute(a)
    myresult=mycursor.fetchall()
    engine.say("here are the following results")
    engine.runAndWait()
    for i in myresult:
        print("registration number:",i[0])
        print("Student name:",i[1])
        print("Contact number:",i[2])
        print("Book Name:",i[3])
        print("Book number:",i[4])
        print("Date of Issue",i[5])
        print("................................")
    main()
def EXIT():
    engine.say("Byee")
    engine.runAndWait()
    exit()
def main():
    print("""
                          LIBRARY MANAGER
    1.ADD BOOK
    2.ISSUE BOOK
    3.SUBMIT BOOK
    4.DELETE BOOK
    5.ADD EXISTING BOOK
    6.DISPLAY BOOKS
    7.DISPLAY ISSUED BOOKS
    8.EXIT THE PROGRAMME
    """)
    choice=input("enter task no:")
    print(".....................................................................")
    if (choice=='1'):
        addbook()
    elif (choice=='2'):
        issueb()
    elif (choice=='3'):
        submit()
    elif (choice=='4'):
        book()
    elif (choice=='5'):
        available()
    elif (choice=='6'):
        dispbook()
    elif (choice=='7'):
        issuedbook()
    elif (choice=='8'):
        EXIT()
    else:
        print("wrong choice.................")
        main()  
main()
engine.stop()
    

