import math

# Function to find 9's complement
def ninesComp(number):

    comp=int("9"*len(str(number))) - number
    return comp

# Function to find 10's complement
def tensComp(num):

    return ninesComp(num)+1


def subtract(num1,num2):
    temp=tensComp(num2)
    num=num1+temp
    n=str(num)
    if (len(n)>len(str(num1))):
        n=list(n)
        n[0]='0'
        n="".join(n)
        return(n)

    elif (num1<num2):
        n=tensComp(int(n))
        return "-"+str(n)

    

def main():

    n='y'
    while n.lower()=='y':
        
        print('\nwelcome! select a Choice.\n')
        print("1.To find 9's Complement of Entered number.")
        print("2.To find 10's Complement of Entered number.")
        print("3.To subtract two numbers.\n")
    
        a=int(input('select option:'))

        if a==1:
            num=int(input("Enter a number."))
            print(f"9's complement is:{ninesComp(num)}")
            
        elif a==2:
            num=int(input("Enter a number."))
            print(f"10's complement is:{tensComp(num)}")

        elif a==3:
            num1=int(input("Enter first number."))
            num2=int(input("Enter second number."))
            result=subtract(num1,num2)
            print("The result of subtraction ",num1,"-",num2," is",result)
            
        else:
            print("Invalid Option")

        n=input('Do you want to continue?(y/n):')
        print()
    print('BYE!')
        
if __name__=='__main__':
    main()


