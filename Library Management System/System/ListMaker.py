def in_list():
    global bookname
    global authorname
    global quantity
    global cost
    bookname=[]
    authorname=[]
    quantity=[]
    cost=[]
    with open("stock.txt","r") as f:
        
        lines=f.readlines()
        lines=[x.strip('\n') for x in lines]
        for i in range(len(lines)):
            ind=0
            for a in lines[i].split(','):
                if(ind==0):
                    bookname.append(a)
                elif(ind==1):
                    authorname.append(a)
                elif(ind==2):
                    quantity.append(a)
                elif(ind==3):
                    cost.append(a.strip("$"))
                ind+=1

def informationofborrower():
    #reading information of borrower from borrower_info.txt
    listofborrow = []
    fileofborrow=open("borrowerInfo.txt",'r')
    borrowfile=fileofborrow.readlines()
    for line in borrowfile:
        listofborrow.append(line.strip("\n").split(",")) #inserting borrower information in 2dlist
    fileofborrow.close()
    return listofborrow
