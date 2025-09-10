# no of words in string
def words(str):
    c=1
    for i in str:
        if i==' ':
            c=c+1
    return c
str=input("Enter the string")
print(words(str))