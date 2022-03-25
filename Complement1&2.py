def binary(n): #convert decimal to binary

    bin=""
    while(n!=0):
        bin = str(n%2) + bin
        n = n//2
    return bin

def flip(a):
    if (a=="0"):
        return "1"
    else:
        return "0"

def OnesComplement(num): #function for finding ones complement
    
    num=binary(num)
    n=len(num)
    ones=""
    for i in range (n):
        ones+=flip(num[i])
    
    return ones

def  TwosComplement(num): # Function to find two's complement

    bitWidth=len(binary(num))
    TC=binary(abs(num - int((num << 1) & 2**bitWidth))) #The two's complement of a binary number is defined 
    return "0"*(bitWidth- len(TC))+TC

def main():
    again='y'
    while again.lower()=="y":
        num=int(input('Enter the number to get Ones and Twos complement.'))
        
        if(num<0):
            print(f"{num} in ones complement representation is: {binary(-num)}")
            print(f"{num} in twos complement representation is: {TwosComplement(-num)}")

        elif(num==0):
            print(f"1's complement of {num} in Binary is: {flip(str(num))} ")
            print(f"2's complement of {num} in Binary is: {num} ")
        else:
            print(f"{num} in binary representation is: {binary(num)}")
            print(f"1's complement of {num} in Binary is: {OnesComplement(num)} ")
            print(f"2's complement of {num} in Binary is: {TwosComplement(num)} ")
            

        again=input('\nDo you want to Continue for another Value.:')
    print('Bye')

if __name__=='__main__':
    main()
