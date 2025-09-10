# find no.of vowels and consonents in str
def countchar(str):
    vc=cc=0
    for x in str:
        if x=='a'or x=='e'or x=='i' or x=='o' or x=='u':
            vc=vc+1
        else:
            cc=cc+1
    print("number of vowelsis",vc)
    print("Number of consonats :",cc)

str=input("Enter the string")
countchar(str)