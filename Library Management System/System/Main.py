import Return
import ListMaker
import DateTime
import Borrow

def start():
    while(True):
        print("        Welcome to the library management system     ")
        print("------------------------------------------------------")
        print("Enter 1. To Display books")
        print("Enter 2. To Borrow a book")
        print("Enter 3. To return a book")
        print("Enter 4. To Display borrower information")
        print("Enter 5. To exit")
        try:
            a=int(input("Select a choice from 1-5: "))
            print()
            if(a==1):
                with open("stock.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
   
            elif(a==2):
                ListMaker.in_list()
                Borrow.borrowBook()
            elif(a==3):
                ListMaker.in_list()
                Return.returnBook()
            elif(a==4):
                with open("borrowerInfo.txt","r") as f:
                    lines=f.read()
                    print(lines)
                    print ()
            elif(a==5):
                print("Thank you user, for using our library management system")
                break
            else:
                print("Please choose and enter a valid number from 1-5")
        except ValueError:
            print("Please input integer as suggested.")
start()
