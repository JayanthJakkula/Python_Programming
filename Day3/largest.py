l=[10,20,50,25,60,37]
a=l[0]
for i in range(len(l)):
    if a<l[i]:
        a=l[i]
b=l[0]
for j in range(len(l)):
     if b<l[j] and b<a:
        b=l[j]
print("second largest number is:",b)

