import DateTime
import ListMaker

def borrowBook():
    success=False
    while(True):
        name=input("Enter the name of the borrower: ")
        if name.isalpha():
            break
        print("Please make sure you enter alphabet from A-Z")
            
    t="Borrow-"+name +".txt"
    with open(t,"w+") as f:
        f.write("               Library Management System  \n")
        f.write("                   Borrowed By: "+name +" \n")
        f.write("    Date: " + DateTime.getDate()+"    Time:"+ DateTime.getTime()+"\n\n")
        f.write("S.N. \t\t Bookname \t      Authorname \n" )
    
    while success==False:
        print("Please select a option below:")
        for i in range(len(ListMaker.bookname)):
            print("Enter", i, "to borrow book", ListMaker.bookname[i])
    
        try:   
            a=int(input())
            try:
                if(int(ListMaker.quantity[a])>0):
                    print("Book is available")
                    with open(t,"a") as f:
                        f.write("1. \t\t"+ ListMaker.bookname[a]+"\t\t  "+ListMaker.authorname[a]+"\n")

                    ListMaker.quantity[a]=int(ListMaker.quantity[a])-1
                    with open("Stock.txt","w+") as f:
                        for i in range(3):
                            f.write(ListMaker.bookname[i]+","+ListMaker.authorname[i]+","+str(ListMaker.quantity[i])+","+"$"+ListMaker.cost[i]+"\n")


                    #multiple book borrowing code
                    loop=True
                    count=1
                    while loop==True:
                        choice=str(input("Do you want to borrow more books? However you cannot borrow same book twice. Press y for yes and n for no."))
                        if(choice.upper()=="Y"):
                            count=count+1
                            print("Please select an option below:")
                            for i in range(len(ListMaker.bookname)):
                                print("Enter", i, "to borrow book", ListMaker.bookname[i])
                            a=int(input())
                            if(int(ListMaker.quantity[a])>0):
                                print("Book is available")
                                with open(t,"a") as f:
                                    f.write(str(count) +". \t\t"+ ListMaker.bookname[a]+"\t\t  "+ListMaker.authorname[a]+"\n")

                                ListMaker.quantity[a]=int(ListMaker.quantity[a])-1
                                with open("Stock.txt","w+") as f:
                                    for i in range(3):
                                        f.write(ListMaker.bookname[i]+","+ListMaker.authorname[i]+","+str(ListMaker.quantity[i])+","+"$"+ListMaker.cost[i]+"\n")
                                        success=False
                            else:
                                loop=False
                                break
                        elif (choice.upper()=="N"):
                            print ("Thank you for borrowing books from us. ")
                            print("")
                            loop=False
                            success=True
                        else:
                            print("Please choose as instructed")
                        
                else:
                    print("Book is not available")
                    borrowBook()
                    success=False
            except IndexError:
                print("")
                print("Please choose book acording to their number.")
        except ValueError:
            print("")
            print("Please choose as suggested.")
