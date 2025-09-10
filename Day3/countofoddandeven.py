def countevenorodd(l):
    ec=oc=0
    for x in l:
        if x%2==0:
            ec=ec+1
        else:
            oc=oc+1
    print("Even numbers in list",ec)
    print("odd numbers in list",oc)
l=[1,2,3,4,5,6,4]
countevenorodd(l)
 