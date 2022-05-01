#Write a program to implement bit-wise Subtraction of two numbers using 2’s complement.
from Logical_adder import adder, twos, bin, dec

def subtractor(a,b):

    if len(a)>len(b):
        b = "0"*(len(a)-len(b))+b
    elif len(b)>len(a):
        a = "0"*(len(b)-len(a))+a

    twos_b=twos(b)
    addition,carry=adder(a,twos_b) 
    if carry==1:
        return addition,0
    else:
        result_twos=twos(addition)
        return result_twos,1

def main():
    print("For subtration.")
    a=int(input("Enter first number: "))
    b=int(input("Enter second number: "))

    result,check= subtractor(bin(a),bin(b))
    if check==0:
        print("\nThe subtraction of these two number is: ", dec(result))
    else:
        print("\nThe subtraction of these two numbers is negative of : ",dec(result))



if __name__=="__main__":
    main()