# payment example
class Payment:
    def pay(self):
        pass
class CashPayment(Payment):
    def pay(self,amt):
        print("Paid {",amt,"} in cash")
class CardPayment(Payment):
    def pay(self,amt):
        print("Paid {",amt,"} using credit/debit")
class UPIPayment(Payment):
    def pay(self,amt):
        print("Paid {",amt,"} using UPI")
cash=CashPayment()
card=CardPayment()
upi=UPIPayment()
l=[cash,card,upi]
for i in l:
    i.pay(500)
    

        
