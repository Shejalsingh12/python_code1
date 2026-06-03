def add(a,b):
    return (a+b)
def sub(a,b):
    return (a-b)
def mul(a,b):
    return a*b
def div(a,b):
    if b!=0:
        return a/b
    else:
        return("invalid input")
def calculator():
    while True:
        print("1.add")
        print("2.sub")
        print("3.mul")
        print("4.division")
        print("5.exit")
        choice=input("choose from 1,2,3,4,5")
        if(choice=="5"):
            print("not possible give some another input")
            break
        if(choice in "1","2","3","4"):
            n1=int(input("enter the 1st no."))
            n2=int(input("enter the 2nd no."))
            if(choice=="1"):
                print(add(n1,n2))
            if(choice=="2"):
                print(sub(n1,n2))
            if(choice=="3"):
                print(mul(n1,n2))
            if(choice=="4"):
                print(div(n1,n2))
            else:
                print("invalid input")
calculator()