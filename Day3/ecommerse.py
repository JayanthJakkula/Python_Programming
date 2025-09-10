cart=[]
print("Cart Operations: 1.Add Product2. Remove Product 3. Search Product4. Display Cart5. Count Products 6. sort 7.clear 8.exit")
while True:
    c=int(input("Enter your choice: "))
    if c==1:
        print("Add product to cart")
        x=input("Enter the product name:")
        cart.append(x)
    elif c==2:
        print("Remove product from cart")
        x=input("Enter product name to delete:")
        for i in cart:
            if i==x:
                cart.remove(i)
                break
            else:
                print("product no there in cart:")
    elif c==3:
        print("Search product from cart")
        x=input("Enter product name to search:")
        for i in cart:
            if i==x:
                print("product found:")
                break
            else:
                print("product no there in cart:")
    elif c==4:
        print("products in cart are:",cart)
    elif c==5:
    
        print("no.of products in cart:",len(cart))
    elif c==6:
        cart.sort()
        print("sorted cart is:",cart)
    elif c==7:
        cart.clear()
        print("clear all products:",cart)
    elif c==8:
        print("Exit")
        break
    else:
        print("invalid choice")
    
        
    
        
    
        
        
