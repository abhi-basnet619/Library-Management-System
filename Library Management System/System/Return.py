import ListMaker
import DateTime
def returnBook():
    name=input("Enter the name of the borrower: ")
    a="Borrow-"+name+".txt"
    try:
        with open(a,"r") as f:
            lines=f.readlines()
            lines=[a.strip("$") for a in lines]
    
        with open(a,"r") as f:
            data=f.read()
            print(data)
    except:
        print("The entered name of the borrower is not in our list")
        returnBook()

    b="Return-"+name+".txt"
    with open(b,"w+")as f:
        f.write("                Library Management System \n")
        f.write("                   Returned by: "+ name+"\n")
        f.write("    Date: " + DateTime.getDate()+"    Time:"+ DateTime.getTime()+"\n\n")
        f.write("S.N.\t\tBookName\t\tCost\n")


    total=0.0
    for i in range(3):
        if ListMaker.bookname[i] in data:
            with open(b,"a") as f:
                f.write(str(i+1)+"\t\t"+ListMaker.bookname[i]+"\t\t$"+ListMaker.cost[i]+"\n")
                ListMaker.quantity[i]=int(ListMaker.quantity[i])+1
            total+=float(ListMaker.cost[i])
            
    print("\t\t\t\t\t\t\t"+"$"+str(total))
    print("Has the return date of the book expired?")
    print("If Yes, press Y and if No, press N")
    stat=input()
    if(stat.upper()=="Y"):
        print("After the expired date,how many days did it take to return the book?")
        day=int(input())
        fine=2*day
        with open(b,"a")as f:
            f.write("\t\t\t\t\tFine: $"+ str(fine)+"\n")
        total=total+fine
    


    print("Final Total: "+ "$"+str(total))
    with open(b,"a")as f:
        f.write("\t\t\t\t\tTotal: $"+ str(total))
    
        
    with open("Stock.txt","w+") as f:
            for i in range(3):
                f.write(ListMaker.bookname[i]+","+ListMaker.authorname[i]+","+str(ListMaker.quantity[i])+","+ListMaker.cost[i]+"\n")
