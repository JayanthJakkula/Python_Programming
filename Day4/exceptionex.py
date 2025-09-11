# exception handling
def division():
    try:
        a=int(input("Enter the numerator:"))
        b=int(input("Enter the denaminator:"))
        c=a/b
        print("division is:",c)
    except:
        print("cannot divisible by error")
    else:
        print("No error in try block")
    finally:
        print("hi")
division()
