# remove no.of duplicates ele in list
def duplicate(l):
    c=0
    for j in range(len(l)):
     for i in l:
            if i==l[j]:
               l.pop(j)
               
    return l
l=[1,2,3,2,3,4,1,6,6,5,5]
print("After removing duplicates in list",duplicate(l))