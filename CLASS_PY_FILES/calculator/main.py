import operations

if __name__ == '__main__':
    while True:
        print(""" 1.addition \n 2.Subtraction \n 3.Multiplication \n 4.Division \n 5.Modulus \n 6.Exponentation \n-1. exit """)

        ch = int(input("Enter the Choice: "))
        if ch==1:
            res = operations.add()
            print(f"The addition of two numbers is {res}")

        elif ch==2:
            res = operations.sub()
            print(f"The Subtraction of two numbers is {res}")

        elif ch==3:
            res = operations.mult()
            print(f"The Multiplication of two numbers is {res}")

        elif ch==4:
            res =operations. div()
            print(f"The Division of two numbers is {res}")

        elif ch==5:
            res = operations.modulus()
            print(f"The Modulus of two numbers is {res}")

        elif ch==6:
            res = operations.exp()
            print(f"The  expotention is {res}")
        elif ch==-1:
            break
        else:
            print("Invalid Choice")
        
