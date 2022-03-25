#Write a program to implement bit-wise addition of two numbers.

def bitwise_addition(a,b):
    while b!=0:
        data=a&b
        a=a^b
        b=data<<1
    return a

def main():
    while(True):
        a=int(input("Enter the first number: "))
        b=int(input("Enter the second number: "))
        res=bitwise_addition(a,b)
        print("Bitwise addition of ",a," and ",b," is: ", res)
        print("In binary bitwise addition of ",bin(a)," and ",bin(b)," is: ",bin(res))

        c=input("\nDo you want to continue.: ")
        if(c.lower()!='y'):
            print("Thanks!")
            break

if __name__=="__main__":
    main()