#delete specific position element
def deletepo(l,pos):
   for i in range(len(l)):
       if i==pos:
            for j in range(pos-1,len(l)-1):
                l[j]=l[j+1]
l=[1,2,3,4,5,6]
x=int(input("Enter the delete position:"))
deletepo(l,x)
print(l[:-1])


  