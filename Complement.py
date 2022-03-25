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
    n=len(num)
    ones=""
    for i in range (n):
        ones+=flip(num[i])
    
    return ones


def  TwosComplement(num): # Function to find two's complement
	
    bin=binary(num)
    n = len(bin)
    
    i = n - 1
    while(i >= 0):
        if (bin[i] == '1'):
            break
        i -= 1

    if (i == -1):
        return '1'+ bin
        
    k = i - 1
    while(k >= 0):
		
		# Just flip the values
        if (bin[k] == '1'):
            bin = list(bin)
            bin[k] = '0'
            bin = ''.join(bin)
        else:
            bin = list(bin)
            bin[k] = '1'
            bin = ''.join(bin)
            
        k -= 1

	#return the modified binary 
    return bin

def main():
    again='y'
    while again.lower()=="y":
        num=int(input('Enter the number to get Ones and Twos complement.'))
        
        if(num<0):
            print(f"{num} in ones complement representation is: {binary(-num)}")
            print(f"{num} in twos complement representation is: {TwosComplement(-num)}")

        elif(num==0):
            print(f"Entered number in Binary is: {num} ")
            num=str(num)
            print(f"1's complement of {num} in Binary is: {flip(num)} ")
            print(f"2's complement of {num} in Binary is: {num} ")
        else:
            print(f"{num} in binary representation is: {binary(num)}")
            print(f"1's complement of {num} in Binary is: {OnesComplement(num)} ")
            print(f"2's complement of {num} in Binary is: {TwosComplement(num)} ")
            

        again=input('\nDo you want to Continue for another Value.(y/n):')
    print('Bye')

if __name__=='__main__':
    main()
