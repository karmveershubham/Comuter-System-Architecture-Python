
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


def flip(a):
    if (a=="0"):
        return "1"
    else:
        return "0"

def OnesComplement(num): #function for finding ones complement
    
    num=binary(num)
    print(f"Entered number in Binary is: {num} ")
    n=len(num)
    ones=""
    for i in range (n):
        ones+=flip(num[i])
    print(f"Ones complement of {num} in Binary is: {ones} ")
    ones=decimal(ones)
    num=decimal(num)
    print(f"Ones complement of {num} in decimal is: {ones} ")

def onesCompNeg(n):  #function for ones complement for negative number.
    ones=-n
    print(f"Ones complement of {n} in Decimal is: {ones} ")
    ones=binary(ones)
    print(f"Ones complement of {n} in Binary is: {ones} ")


def main():
    again='y'
    while again.lower()=="y":
        num=int(input('Enter the number to get Ones complement.'))
        
        if(num<0):
            onesCompNeg(num)
        elif(num==0):
            print(f"Entered number in Binary is: {num} ")
            num=str(num)
            print(f"Ones complement of {num} in Binary is: {flip(num)} ")
        else:
            OnesComplement(num)

        again=input('\nDo you want to Continue for another Value.(y/n):')
    print('Bye')

if __name__=='__main__':
    main()
