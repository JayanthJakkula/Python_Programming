class BankAccount():
    def __init__(self,bal=0):
        self.__bal=bal
    def deposit(self,amt):
        self.__bal+=amt
    def withdraw(self,amt):
        if amt<self.__bal:
          self.__bal=self.__bal-amt
        else:
            print("insufiicient balance")
    def get_bal(self):
        print("Avialable balance is: ",self.__bal)
ob=BankAccount(1000)
ob.deposit(1000)
ob.withdraw(500)
ob.get_bal()
