import math

def calc():
    print("**************************Calculator*****************************")
    print("Press 'S' for Scientific Calculator & 'N' for Standard Calculator")
    choice=input("Enter Your Choice : ")
    if choice == 'N':
        print("***********STANDARD CALCULATOR**************")
        print("""1. Addition
2. Substraction
3. Multiplication
4. Division""")
        cal = int(input("Enter a Number"))
        if cal == 1:
            sum = 0
            print("****Addition****")
            a = int(input("Enter the no. of Elements to be added :"))
            for i in range(a):
                b = eval(input("Enter The Numbers : "))
                sum = sum + b
            print(f"The Sum of the given Numbers are : {sum}")
        elif cal == 2:
            s = 0
            print("****Substraction****")
            a = int(input("Enter the no. of Elements to be Substracted:"))
            for i in range(a):
                b = eval(input("Enter The Numbers : "))
                s = s - b
            print(f"The Sum of the given Numbers are : {s}")
        elif cal == 3:
            s = 0
            print("****Multiplication****")
            a = int(input("Enter the no. of Elements to be Multiplied :"))
            for i in range(a):
                b = eval(input("Enter The Numbers : "))
                s = s * b
            print(f"The Sum of the given Numbers are : {s}")
        elif cal == 4:
            print("****Division****")
            a = int(input("Enter Divident : "))
            b = int(input("Enter Divisor : "))
            print(f"The Quotient of the given 2 no. is {a // b}")
            print(f"The remainder of the given 2 no, is {a % b}")
        else:
            print("Invalid Input")
        print("Do you want To Do any Other Calculation Y/N : ")
        op = input("Enter Your Choice : ")
        if op == "Y":
            calc()
        elif op == "N":
            print("Thanks For Using Our Calculator")
    elif choice == 'S':
        print("***********SCIENTIFIC CALCULATOR**************")
        print("""1. Addition
2. Substraction
3. Multiplication
4. Division
5. Square Root
6. Power 
7. Sine
8. Cosine
9. Tan
10. Log Base 10
11. Logarithm""")
        cal=int(input("Enter a Number"))
        if cal==1:
            sum=0
            print("****Addition****")
            a = int(input("Enter the no. of Elements to be added :"))
            for i in range(a):
                b = eval(input("Enter The Numbers : "))
                sum = sum + b
            print(f"The Sum of the given Numbers are : {sum}")
        elif cal==2:
            s = 0
            print("****Substraction****")
            a = int(input("Enter the no. of Elements to be Substracted:"))
            for i in range(a):
                b = eval(input("Enter The Numbers : "))
                s = s - b
            print(f"The Sum of the given Numbers are : {s}")
        elif cal==3:
            s = 1
            print("****Multiplication****")
            a = int(input("Enter the no. of Elements to be Multiplied :"))
            for i in range(a):
                b = eval(input("Enter The Numbers : "))
                s = s*b
            print(f"The Sum of the given Numbers are : {s}")
        elif cal==4:
            print("****Division****")
            a = int(input("Enter Divident : "))
            b = int(input("Enter Divisor : "))
            print(f"The Quotient of the given 2 no. is {a//b}")
            print(f"The remainder of the given 2 no, is {a%b}")
        elif cal==5:
            a = int(input("Enter the Number : "))
            print(f"The Square root of the Given No. is {math.sqrt(a)}")
        elif cal==6:
            a = int(input("Enter Base : "))
            b = int(input("Enter Power : "))
            print(f"{a} to the power {b} is {math.pow(a,b)}")
        elif cal==7:
            a= eval(input("Enter the Value in Radian :"))
            print(f"The Sine Value of the given no is {math.asin(a)}")
        elif cal==8:
            a = eval(input("Enter the Value in Radian :"))
            print(f"The Cosine Value of the given no is {math.acos(a)}")
        elif cal==9:
            a = eval(input("Enter the Value in Radian :"))
            print(f"The Tan Value of the given no is {math.tan(a)}")
        elif cal==10:
            a = eval(input("Enter the Value :"))
            print(f"The Log base 10 Value of the given no is {math.log10(a)}")
        elif cal==11:
            a = eval(input("Enter the Base :"))
            b = eval(input("Enter the Value :"))
            print(f"The Sine Value of the given no is {math.log(b,a)}")
        else:
            print("Invalid Input")
    print("Do you want To Do any Other Calculation Y/N : ")
    op=input("Enter Your Choice : ")
    if op=="Y":
        calc()
    elif op=="N":
        print("Thanks For Using Our Calculator")
if __name__ == "__main__" :
    calc()


