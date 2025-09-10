"""Management System in Python. The system should store books in a dictionary where:
Key → Book ID
Value → Book Title
Write a Python program to perform the following operations using Dictionaries:
Add a book to the library (Book ID, Title).
Remove a book using Book ID.
Search for a book by Book ID and display the title.
Update the title of a book (e.g., correction in title).
Display all books in the library.
Count the total number of books in the library.
Check if a book title exists in the library (reverse lookup)"""
def library():
    d={}
    n=int(input("Enter no.of books:"))
    for i in range(n):
        x=input("Enter the book id :")
        y=input("Enter boo title :")
        d[x]=y
    x=input("Enter the book id to delete")
    d.pop(x)
    a=input("Enter the book id to search")
    for i in d.keys():
        if a==i:
            print("the book is present in library")
            break
        
    else:
        print("not there")
    y=input("enter the new book title:")
    b=input("Enter the bood id for which book title should be change:")
    d.update({b:y})
    print("tot no.of books are :",len(d.keys()))
    c=input("enter the new book title:")
    for i in d.keys():
        if c==d[i]:
            print("it is present")
            break
    else:
        print("it is not present")

library()


    
    
    