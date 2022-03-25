def selective_clear(a,b):  #Write a program to implement Selective Clear logical operation using bit-wise operators
    return (~b) & a


def main():

    print("To perform selective clear.\n")
    while(True):
        
        a=int(input("Enter the first number."))
        b=int(input("Enter the second number"))

        res=selective_clear(a,b)

        print("The selective clear of ",a," with respect to ",b," is: ",res )
        print("In binary selective clear of ",bin(a)," with respect to ",bin(b)," is:" ,bin(res))

        c=input("\nDo you want to continue.: ")
        if(c.lower()!='y'):
            print("Bye!")
            break
    
if __name__=="__main__":
    main()