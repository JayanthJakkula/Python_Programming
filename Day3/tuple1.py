def tuple1():
    l=[]
    for i in range(3):
        x=input("Enter student name:")
        r=input("Enter roll no:")
        m=int(input("Enter marks:"))
        t=(x,r,m)
        l.append(t)
    a=l[0][2]
    for i in range(3):
        if a<l[i][2]:
            a=l[i][2]
    
    print(l)
    print("maximum marks are",a)
    
tuple1()

            