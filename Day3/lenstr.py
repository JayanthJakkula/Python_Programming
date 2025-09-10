# find len of string
def lengthofstring(str):
    c=0
    for i in str:
        c=c+1
    return c 
str=input("Enter the string:")
print(lengthofstring(str))
def comparestr(str1,str2):
    if str1==str2:
        print("they are same")
    else:
        print("they are not")
str1=input("Enter the 1st string:")
str2=input("Enter the 2nd string:")
print(comparestr(str1,str2))
def concate(str1,str2):
    str=str1+str2
    return str
str1=input("Enter the 1st string:")
str2=input("Enter the 2nd string:")
print(concate(str1,str2))

