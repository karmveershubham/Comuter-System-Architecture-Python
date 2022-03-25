#Right and left shift using bitwise operator.

def rightshift(a,b): #rightshift a by b
    return a>>b

def lefttshift(a,b): #leftshift a by b
    return a<<b

def main():

    while(True):
        
        print("\nTo perform: ")
        print("1. Right shift of first number by second. ")
        print("2. Left shift of  first number by second. ")

        while(True):
            print("\nEnter a choice.")
            n = int(input())

            if(n==1):
                a=int(input("Enter first number  "))
                b=int(input("Enter second number  "))
                if(b<0):
                    print("Enter Positive number only")
                else:
                    print(a, " >> ", b ," = ", rightshift(a,b))
                break

            elif(n==2):
                a=int(input("Enter first number  "))
                b=int(input("Enter second number  "))
                if(b<0):
                    print("Enter Positive number only")
                else:
                    print(a, " << ",b," = ", lefttshift(a,b))
                break
            else:
                print("WRONG CHOICE ")
                print("Enter Again")
            


        c=input("\nDo you want to continue.: ")
        if(c.lower()!="y"):
            print("Thanks")
            break

if __name__=='__main__':
        main()


