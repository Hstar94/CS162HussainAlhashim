#Banking Test 1.1
import matplotlib.pyplot as plt
class Account:
    
    def __init__(self,number,fname,lname,balance,opens):
        
        self.opened=opens #when open is false means account is closed
        self.accountNumber=number
        self.firstName=fname
        self.lastName=lname
        self.balance=balance
        
    def deposit(self,amount):
        self.balance = self.balance + amount

    def withdraw(self,amount):
        if amount > self.balance :
             print("You don't have sufficient balance")
        else :         
             self.balance = self.balance - amount

    def displayInfo(self):
        print(F"Account number:{self.accountNumber} \nFirst Name:{self.firstName} \nLast Name:{self.lastName} \nBalance:{self.balance}\n")

    def getAccountNumber(self):

        return self.accountNumber

    def getBalance(self):

        return self.balance

class Checking(Account):
    pass
    
        
class Saving(Account):

    def addInterest(self):
        amount = self._balance * 5 / 100.0 #interest amount
        self.balance=self.balance+amount
        

    
class Bank:
    
    def __init__(self):
        self.lastaccountNumber=12567    #Starting Account number
        self.checkingAccounts=[]
        self.savingAccounts=[]
        self.readFiles()
        
        for a in self.checkingAccounts:
            if(int(a.accountNumber)>self.lastaccountNumber):
                self.lastaccountNumber=int(a.accountNumber)+1
        
        for a in self.savingAccounts:
            if(int(a.accountNumber)>self.lastaccountNumber):
                self.lastaccountNumber=int(a.accountNumber)+1
        
    
    def openAccount(self):
        fname=input("First name: ")
        lname=input("Last name: ")
        
        while(True):
            balance=input("Initial balance: ")
            try:
                balance=float(balance)
                break
            except:
                print("Balance must be a number")
                
        accountNum=self.lastaccountNumber
        self.lastaccountNumber+=1
        
        accountType=input("Account type: (C)hecking/(S)aving: ")
        if(accountType.lower()=="c"):
            account=Checking(str(accountNum),fname,lname,balance,True)
            self.checkingAccounts.append(account)
        else:
            account=Saving(str(accountNum),fname,lname,balance,True)
            self.savingAccounts.append(account)
 
        print("Account opened")
        account.displayInfo()
            
    
        
    def writeFiles(self):
        file=open("saving.txt", "w")
        for account in self.savingAccounts:
            file.write(F"{account.accountNumber},{account.firstName},{account.lastName},{account.balance},{account.opened}\n")
        file.close()
    
        file=open("checking.txt", "w")
        for account in self.checkingAccounts:
            file.write(F"{account.accountNumber},{account.firstName},{account.lastName},{account.balance},{account.opened}\n")
        file.close()
        
    
    def readFiles(self):
        try:
            file=open("saving.txt", "r")
        except:
            print("Files doesnot exists")
            return

        for line in file:
            parts=line.split(',')
            account=Saving(parts[0],parts[1],parts[2],float(parts[3]),bool(parts[4]))
            self.savingAccounts.append(account)
        file.close()     

        file=open("checking.txt", "r")

        for line in file:
            parts=line.split(',')
            account=Checking(parts[0],parts[1],parts[2],float(parts[3]),bool(parts[4]))
            self.checkingAccounts.append(account)
        file.close() 
        #storing sorted lists be last name
        self.__Quicksort(self.checkingAccounts,0,len(self.checkingAccounts)-1)
        self.__Quicksort(self.savingAccounts,0,len(self.savingAccounts)-1)
        
    
       
    def closeAccount(self):
        while(True):
            acctype=input("Enter account type: (C)hecking/(S)aving: ")
            if(acctype.lower()=="c" or acctype.lower()=="s"):
                break
            else:
                print("Invalid account type entered")
        accNum=input("Enter account number: ")    
        account=self.searchAccount(accNum,acctype)
        if(account is None):
            print("Account does not exists")
        else:
            account.opened=False
            print("Account closed")
        
    def withdraw(self):
        acctype=""
        while(True):
            acctype=input("Enter account type: (C)hecking/(S)aving: ")
            if(acctype.lower()=="c" or acctype.lower()=="s"):
                break
            else:
                print("Invalid account type entered")
        accNum=input("Enter account number: ")    
        account=self.searchAccount(accNum,acctype)
        if(account is None):
            print("Account does not exists")
        else:
            if(account.opened):
                amount=input("Enter amount to withdraw: ")
                try:
                    amount=float(amount)
                    account.withdraw(amount)
                    print("{0} withdrawed to account number: {1}".format(amount,account.getAccountNumber()))
                except:
                    print("Invalid amount entered or Invalid input type")
            else:
                print("Account is closed, you can't proceed")
        
    def deposit(self):
        acctype=""
        while(True):
            acctype=input("Enter account type: (C)hecking/(S)aving: ")
            if(acctype.lower()=="c" or acctype.lower()=="s"):
                break
            else:
                print("Invalid account type entered")
        accNum=input("Enter account number: ")    
        account=self.searchAccount(accNum,acctype)
        if(account is None):
            print("Account does not exists")
        else:
            if(account.opened):
                amount=input("Enter amount to deposit: ")
                try:
                    amount=float(amount)
                    account.deposit(amount)
                    print("${0} deposited to account number: {1}".format(amount,account.getAccountNumber()))
                except:
                    print("Invalid amount entered")
            else:
                print("Account is closed, you can't proceed")
        
    def searchAccount(self,accNum,acctype):
 
        if(acctype.lower()=="c"):
            
            for i in range(len(self.checkingAccounts)):
                if(self.checkingAccounts[i].accountNumber ==accNum):
             
                    return self.checkingAccounts[i]
        else:
            for i in range(len(self.savingAccounts)):
                if(self.savingAccounts[i].accountNumber ==accNum):
                    return self.savingAccounts[i]
            
        return None
    
    def accountNumber(self):
        while(True):
            acctype=input("Enter account type: (C)hecking/(S)aving: ")
            if(acctype.lower()=="c" or acctype.lower()=="s"):
                break
            else:
                print("Invalid account type entered")
        lname=input("Enter last name: ")
        if(acctype.lower()=="c"):
            for i in range(len(self.checkingAccounts)):
                if(self.checkingAccounts[i].lastName ==lname):
                    print("Account number is: ",self.checkingAccounts[i].getAccountNumber())
                    return
        else:
            for i in range(len(self.savingAccounts)):
                if(self.savingAccounts[i].lastName ==lname):
                    print("Account number is: ",self.savingAccounts[i].getAccountNumber())
                    return
        print("No account found with this last name")
    def createPlots(self):
        names = ['Checking Account','Saving Account']
        values = [0,0]
        #calculating total amounts in each type of account
        for account in self.checkingAccounts:
            values[0]+=account.getBalance()
        
        for account in self.savingAccounts:
            values[1]+=account.getBalance()
        

        plt.figure(figsize=(9, 3))

        plt.subplot(131)
        plt.bar(names, values, color = 'r' + 'b')
       
        plt.suptitle('Total amount plots')
        plt.show()
    
    
    #quick sort on last names
    def __Partition(self,accounts, lowIndex, highIndex):
        #Pick middle element as pivot
        midpoint = int(lowIndex + (highIndex - lowIndex) / 2)
        pivot = accounts[midpoint].lastName

        done = False
        while (not done):
            #Increment lowIndex while numbers[lowIndex] < pivot
            while (accounts[lowIndex].lastName < pivot):
                lowIndex += 1
          

            #Decrement highIndex while pivot < numbers[highIndex]
            while (pivot < accounts[highIndex].lastName):
                highIndex -= 1
          

            #If zero or one elements remain, then all numbers are partitioned. Return highIndex.
            if (lowIndex >= highIndex):
                done = True
          
            else:
             # Swap numbers[lowIndex] and numbers[highIndex]
                temp = accounts[lowIndex]
                accounts[lowIndex]= accounts[highIndex]
                accounts[highIndex] = temp

                #Update lowIndex and highIndex
                lowIndex += 1
                highIndex -= 1
          
       

        return highIndex
    

    def __Quicksort(self,accounts, lowIndex, highIndex):
        #Base case: If the partition size is 1 or zero 
        #elements, then the partition is already sorted
        if (lowIndex >= highIndex):
            return
       

        #Partition the data within the dic. Value lowEndIndex returned from partitioning is the index of the low partition's last element.
        lowEndIndex = self.__Partition(accounts, lowIndex, highIndex)

        #Recursively sort low partition (lowIndex to lowEndIndex) 
        #and high partition (lowEndIndex + 1 to highIndex)
        self.__Quicksort(accounts, lowIndex, lowEndIndex)
        self.__Quicksort(accounts, lowEndIndex + 1, highIndex)
     
    def printLists(self):
        print("Saving account\n")
        for account in self.savingAccounts:
            account.displayInfo()
            
        print("Checking account\n")
        for account in self.checkingAccounts:
            account.displayInfo()
        
def main():
    
    bank=Bank()
        
    while(True):

        option=input("Choose option:\n(1) Open Account \n(2) Close Account\n"+
                    "(3) Deposit amount\n(4) Withdraw amount\n(5) Get account number\n"+
                    "(6) Generate plots\n(7) Print Lists \n(8) Quit\n --> ")

        if(option=="1"):
            bank.openAccount()
        elif(option=="2"):
            bank.closeAccount()
        elif(option=="3"):
            bank.deposit()
        elif(option=="4"):
            bank.withdraw()
        elif(option=="5"):
            bank.accountNumber()
        elif(option=="6"):
            bank.createPlots()
        elif(option=="7"):
            bank.printLists()
        elif(option=="8"):
            bank.writeFiles()
            break
        else:
            print("Invalid option entered")    
main()

