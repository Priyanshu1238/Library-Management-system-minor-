#                   ************* FRONTEND *************
print("******************** BOOKSTORE MANAGEMENT SYSTEM ********************")
def main():
    import backend
    print("1. ADD BOOK")
    print("2. SEARCH BOOK")
    print("3. DELETE BOOK")
    print("4. UPDATE BOOK")
    print("5. BUYING BOOK")
    print("6. DISPLAY BOOKS")
    print("7. EXIT")
    run=True
    while run:
        x=int(input("ENTER THE OPTION THAT YOU WANT :"))
        print("                                       ")
        print("                                       ")
        if x==1:
            print("                   ADD BOOK----->")
            print("                                       ")
            print("                                       ")
            backend.addbook()
        elif x==2:
            print("                 SEARCH BOOK----->")
            print("                                       ")
            print("                                       ")
            backend.search()
        elif x==3:
            print("                 DELETE BOOK----->")
            print("                                       ")
            print("                                       ")
            backend.delete()
        elif x==4:
            print("                 UPDATE BOOK----->")
            print("                                       ")
            print("                                       ")
            backend.update()
        elif x==5:
            print("                 BUYING BOOK----->")
            print("                                       ")
            print("                                       ")
            backend.buying_book()
        elif x==6:
            print("                 ALL BOOKS----->")
            print("                                       ")
            print("                                       ")
            backend.display()
        elif x==7:
            backend.close()
            break
        else:
            print("                 WRONG INPUT")
main()  
