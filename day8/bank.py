from abc import ABC,abstractmethod
class Account:
    @abstractmethod
    def get_balance():
        pass

    @abstractmethod
    def deposite():
        pass

    @abstractmethod
    def withdraw():
        pass


#polymorphism

class SavingsAccount(Account):
    __balance=0

    def get_balance(self):
        return self.__balance


    def deposite(self,amount):
        self.__balance+=amount


    def withdraw(self,amount):
        self.__balance-=amount



class CurrentAccount(Account):

    __balance=0

    withdraw_limit=0

    def withdraw_limit(self,limit):
        self.withdraw_limit=limit

    def get_balance(self):
        return self.__balance


    def deposite(self,amount):
        self.__balance+=amount


    def withdraw(self,amount):
        self.__balance-=amount


class Bank:
    owner="bank"
    act_no=0

    def __init__(self,name,num,account_type="SavingsAccount"):
        self.owner=name
        self.act_no=num

        if account_type == "SavingsAccount":
            self.account = SavingsAccount()

        if account_type == "CurrentAccount":
            self.account = CurrentAccount()

class Manager:

    def get_customer_info(self,bankaAccount:Bank):
        return f"NAME : {bankaAccount.owner}"
        return f"ACCOUNTNUMBER : {bankaAccount.act_no}"
        print("ACCOUNT TYPE : ",end="")
        if type( bankaAccount.account)==SavingsAccount:
           return "SAVINGS ACCOUNT"

        else:
            return "CURRENT ACCOUNT"

# with open("./bankdetail.txt","a") as file:
# ram = Bank("Ram" , 1 , "SavingsAccount")
# ram.account.deposite(18)
# sam=Bank("sam",2,"CurrentAccount")
# sam.account.withdraw(98)


dk=Manager()
with open("./bankdetail.txt","a") as file:
    ram = Bank("Ram" , 1 , "SavingsAccount")
    # ram.account.deposite(18)
    sam=Bank("sam",2,"CurrentAccount")
    # sam.account.withdraw(98)
        
    file.write("<=====RAM ACCOUNT=====>")
    file.write("\n\n")
    file.write(dk.get_customer_info(ram))
    file.write("\n")
    file.write(ram.account.deposite(18))

    file.write("\n\n")
    file.write("<=====SAM ACCOUNT=====>")
    file.write("\n\n")
    file.write(dk.get_customer_info(sam))
    file.write("\n")
    file.write(sam.account.withdraw(98))

    file.close()

    print(dk.get_customer_info(ram))
    print(dk.get_customer_info(sam))

        
    