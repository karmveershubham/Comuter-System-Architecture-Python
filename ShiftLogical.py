#Right and left shift using logical operators.

def binary(n): #convert decimal to binary
    bin=""
    while(n!=0):
        bin = str(n%2) + bin
        n = n//2
    
    return bin


def decimal(n): #convert binary to decimal
    dec=0
    j=len(n)-1
    for i in n:
        dec = dec + int(i)*2**j
        j-=1
        
    return dec
        

def rightshift(a,b): #rightshift a by b

    a=binary(a)
    a=a[:len(a)-b]   #shifting values
    print("Rightshift value in binary: "+a)
    a=decimal(a)
    return a
    

def lefttshift(a,b): #leftshift a by b

    a=binary(a)
    a=a+'0'*b
    print("Leftshift value in binary: "+ a )
    a=decimal(a)
    return a

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
                if(a<0 or b<0):
                    print("Enter Positive number only")
                else:
                    print(a, " >> ", b ," = ", rightshift(a,b))
                break

            elif(n==2):
                a=int(input("Enter first number  "))
                b=int(input("Enter second number  "))
                if(a<0 or b<0):
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


