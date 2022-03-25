def And(a,b):
    AND=a & b
    return AND

def Or(a,b):
    OR=a|b
    return OR

def Xor(a,b):
    XOR=a ^ b
    return XOR


def main():

    while(True):
        while(True):
            a=int(input("Enter first number  "))
            b=int(input("Enter second number  "))

            if(a<0 or b<0):
                print("Enter Positive number only")
            else:
                break
        
        print("\nTo perform : ")
        print("1. AND Operation between Two number")
        print("2. OR  Operation between Two number")
        print("3. XOR Operation between Two number")

        while(True):
            print("\nEnter a choice.")
            n = int(input())

            if(n==1):
                print(a, " AND ", b ," = ", And(a,b))
                break
            elif(n==2):
                print(a, " OR ",b," = ", Or(a,b))
                break
            elif(n==3):
                print(a, " XOR ",b," = ", Xor(a,b))
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
