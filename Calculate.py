print("==== CALCULATE ====")


print("1.   Addition")
print("2.   Subtraction")
print("3.   Multiple")
print("4.   Division")
print("5.   Floor division")
print("6.   Modulas")
print("7.   Power")
print("8.   Square")


choice=int(input("Enter the Choise Number:-"))


if(choice==8):
    x=float(input("Enter The number:-"))
    result= x**2
    print("Result:",result)

else:
    x=float(input("Enter The First Value:-"))
    y=float(input("Enter The Second Value:-"))


    if(choice==1):
        result=x+y
        print("Result:",result)

    elif(choice==2):
        result=x-y
        print("Result:",result)

    elif(choice==3):
        result=x*y
        print("Result:",result)

    elif(choice==4):
        if(y==0):
            print("You Cannot division by zero")
        else:
            result=x/y
            print("Result:",result)

    elif(choice==5):
        if(y==0):
            print("You Cannot Floor Division by zero")
        else:
            result=x//y
            print("Result:",result)

    elif(choice==6):
        if(y==0):
            print("You Cannot Calculate Modulas to zero")
        if(y > x):
            print("You Cannot Calculate Modulas")
        else:
            result=x % y
            print("Result:",result)

    elif(choice==7):
        result=x**y
        print("Result:",result)

    else:
        print("Invaild Choice")
    

