def selective_complement(a,b):   #Write a program to implement Selective Complement logical operation using bit-wise operators.
    return a^b

def main():

    while(True):
        a=int(input("Enter the first number."))
        b=int(input("Enter the second number"))

        res=selective_complement(a,b)

        print("The selective complement of ",a," and  ",b," is: ",res )
        print("In binary selective complement of ",bin(a)," and ",bin(b)," is: ",bin(res) )

        c=input("\nDo you want to continue.: ")
        if(c.lower()!='y'):
            print("Bye!")
            break
    
if __name__=="__main__":
    main()