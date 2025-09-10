# find no.of apha,number and special charaters in str
def countchar(str):
    ac=dc=sc=0
    for x in str:
        if x.isalpha():
            ac=ac+1
        elif x.isdigit():
            dc=dc+1
        else:
            sc=sc+1
    print("number of alphacharter is",ac)
    print("Number of digits :",dc)
    print("number of special charaters:",sc)
str=input("Enter the string")
countchar(str)
