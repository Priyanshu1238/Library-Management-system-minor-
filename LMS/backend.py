#                       ********************** BACKEND*****************
import mysql.connector as mysql
conn=mysql.connect(host="localhost",user="root",password="Arun@2001",database="db")

def addbook():
    ID=input("Enter the ID :")
    TITLE=input("Enter the Title :")
    AUTHOR=input("Enter the Author :")
    YEAR=input("Enter the Year :")
    ISBN_CODE=input("Enter the ISBN code :")
    PRICE=input("Enter the Price :")
    DISCOUNT=input("Enter the Discount :")
    AVAILABILITY=input("Enter the Total no. of book available :")
    data=(ID,TITLE,AUTHOR,YEAR,ISBN_CODE,PRICE,DISCOUNT,AVAILABILITY)
    sql='insert into book1 values(%s,%s,%s,%s,%s,%s,%s,%s)'
    c=conn.cursor()
    c.execute(sql,data)
    conn.commit()
    print('''
          ******************** BOOK ADDED SUCESSFULLY ********************''')

def delete():
    delete_id=input("ENTER ID :")
    a='delete from book1 where id=%s'
    data=(delete_id,)
    c=conn.cursor()
    c.execute(a,data)
    conn.commit()
    print('''
          ******************** DATA DELETED SUCESSFULLY ********************''')

def search():
    l=input("ENTER ID :")
    a=('select * from book1 where id=%s')
    data=(l,)
    c=conn.cursor()
    c.execute(a,data)
    myresult=c.fetchall()
    for i in myresult:
        print("BOOK NAME :",i[1])
        print("AUTHOR :",i[2])
        print("YEAR :",i[3])
        print("ISBN CODE :",i[4])
        print("PRICE :",i[5])
        print("DISCOUNT :",i[6])
        print("AVAILABLE BOOKS :",i[7])
        print('''
              ******************** DATA SEARCHED SUCESSFULLY ********************''')

def update():
    l=input("ENTER ID :")
    a=('select * from book1 where id=%s')
    data=(l,)
    c=conn.cursor()
    c.execute(a,data)
    myresult=c.fetchall()
    for i in myresult:
        print("BOOK ID :",i[0])
        print("BOOK NAME :",i[1])
        print("AUTHOR :",i[2])
        print("YEAR :",i[3])
        print("ISBN CODE :",i[4])
        print("PRICE :",i[5])
        print("DISCOUNT :",i[6])
        print("AVAILABLE BOOKS :",i[7])
        print('''
              ******************** MODIFY THE DATA ********************''')
                                             
        ID=input("Enter the ID :")
        TITLE=input("Enter the Title :")
        AUTHOR=input("Enter the Author :")
        YEAR=input("Enter the Year :")
        ISBN_CODE=input("Enter the ISBN code :")
        PRICE=input("Enter the Price :")
        DISCOUNT=input("Enter the Discount :")
        AVAILABILITY=input("Enter the Total no. of book available :")
        data=(TITLE,AUTHOR,YEAR,ISBN_CODE,PRICE,DISCOUNT,AVAILABILITY,ID)
        sql='update book1 set title=%s,author=%s,year=%s,isbn=%s,price=%s,discount=%s,book_available=%s where id=%s'
        c=conn.cursor()
        c.execute(sql,data)
        conn.commit()

        print('''
              ******************** DATA UPDATED SUCESSFULLY ********************''')

def display():
    a=('select * from book1')
    c=conn.cursor()
    c.execute(a)
    myresult=c.fetchall()
    for i in myresult:
        print("BOOK ID :",i[0])
        print("BOOK NAME :",i[1])
        print("AUTHOR :",i[2])
        print("YEAR :",i[3])
        print("ISBN CODE :",i[4])
        print("PRICE :",i[5])
        print("DISCOUNT :",i[6])
        print("AVAILABLE BOOKS :",i[7])
        print("-----------------------------------------------------------------------")

def buying_book():
    l=input("ENTER ID :")
    a=('select * from book1 where id=%s')
    data=(l,)
    c=conn.cursor()
    c.execute(a,data)
    myresult=c.fetchall()
    for i in myresult:
        print("BOOK NAME :",i[1])
        print("AUTHOR :",i[2])
        print("YEAR :",i[3])
        print("ISBN CODE :",i[4])
        print("PRICE :",i[5])
        print("DISCOUNT :",i[6])
        c=i[7]
    nb=int(input("ENTER THE NUMBER OF BOOKS BUYING :"))
    if c>nb:
        alter(l,-nb)
    else:
        print("SORRY....,BOOK IS NOT AVAILABLE IN SUFFICIENT QUANTITY!!!!!!!!!!!!!!!!!!!!!!!!!!")
    
    print('''
          ******************** BOOK SOLD ********************''')

def alter(l,u):
    a='select book_available from book1 where id=%s'
    data=(l,)
    c=conn.cursor()
    c.execute(a,data)
    myresult=c.fetchone()
    t=myresult[0] + u
    sql='update book1 set book_available=%s where id=%s'
    d=(t,l)
    c.execute(sql,d)
    conn.commit()
    
def close():
    print('''
          ******************** THANK YOU ********************''')


        

    
    
    
    
       
    

    
    



    
