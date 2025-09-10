# character count
def charcount(str):
    l=list(str)
    for x in range(len(l)-1):
        c=0
        for y in range(1,len(l)):
         if l[x]==l[y]:
            c=c+1
            l.remove(l[x])
    print(l[x],c+1)
str=input("Enter the string")
charcount(str)


        