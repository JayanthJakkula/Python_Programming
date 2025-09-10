# insert ele into set
def set1():
    s=set()
    n=int(input("Enter no.of elemnts:"))
    for i in range(n):
        x=input("Enter the element")
        s.add(x)
        
    return s
print("set contains:",set1())
