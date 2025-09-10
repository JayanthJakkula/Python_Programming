def discount(p,dper):
    return p-(p*dper/100)
def gst(p,gper=18):
    return p+(p*gper)/100
def invoice(cart,dper=10,gper=18):
    s=0
    print(cart)
    for i in cart.keys():
        s=s+cart[i]
    print("Subtotal:",s)
    a=discount(s,10)
    print("After 10% discount:",a)
    print("After 18% gst:",gst(a))
    print("----------")
    print("thank you for shopping")
    
           