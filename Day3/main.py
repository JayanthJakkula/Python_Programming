# main function
import ecommerse_util
cart={}
n=int(input("Enter no.of carts:"))
for i in range(n):
    x=input("Enter the name:")
    y=int(input("Enter price :"))
    cart[x]=y
ecommerse_util.invoice(cart)