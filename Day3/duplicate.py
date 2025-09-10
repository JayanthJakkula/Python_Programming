# count no.of duplicates ele in list
def duplicate(l):
    c=0
    for i in range(len(l)):
        for j in range(i+1,len(l)):
            if l[i]==l[j]:
               c=c+1
               
    return c
l=[1,2,3,2,3,4,1,6,6,5,5]
print("No.of duplicates in list",duplicate(l))
