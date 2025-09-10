# occurance of character in string
def occurance(str,a):
    c=0
    
    for i in str:
        if i==a:
            c=c+1
    if c>0:
        print("it is occured:",c,"times")
    else:
        print("it is not found")
str=input("Enter the string")
a=input("Enter a character to search")
occurance(str,a)