import mysql.connector as mysc
con=mysc.connect(host='localhost',user='root',passwd='0020',database='emp')
cur=con.cursor()

while True:
    # This function is under development.
    # Change of table name in all functions is next.
    def create(t_name):
        com=input("Enter your SQL command to create table: ")
        if con.is_connected():
            cur.execute(com)
            con.commit()

    def commands():
        sid=int(input('Enter student id: '));
        sname=input("Enter student name: ");
        marks=int(input("Enter marks: "));
        qu="insert into student values(%s,%s,%s)"
        cur.execute("insert into student values(%s,'%s',%s)"%(sid,sname,marks))
        con.commit()

    print("Enter 1 to create table.")
    choice=int(input("Enter 2 to enter values.\nEnter 3 to display values of table: "))
    if choice==1:
        create(name)
    elif choice==2:
        commands()
    elif choice==3:
        #n=int(input("Enter no. of records to display: "))       #Limited records to display.
        cur.execute("select * from student;")
        #data=cur.fetchmany(n)
        data=cur.fetchall()
                                                                    # Display all records.
                                                                    #Simmilarly:
                                                                        #1. fetchone() [display the first one]"""
        name=input("enter name: ")
        for i in data:
            if i[1]==name:
                print(i)
    loop=input("Enter y to continue: ")
    if loop!='y':
        break
