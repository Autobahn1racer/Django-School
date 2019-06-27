import mysql.connector as mysc
con=mysc.connect(host='localhost',user='root',passwd='0020',database='emp')
cur=con.cursor()

while True:
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

    print("Enter 1 to create table.")
    choice=int(input("Enter 2 to enter values."))
    if choice==1:
        create(name)
    elif choice==2:
        commands()
    loop=input("Enter y to continue: ")
    if loop!='y':
        break
