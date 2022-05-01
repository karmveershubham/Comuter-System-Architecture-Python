#WAP to implement bitwise addition of two number.
def flip(n):
    if n=="1":
        return "0"
    else:
        return"1"

def dec(n):
    dec=0
    j=len(n)-1
    for i in n:
        dec+=int(i)*2**j
        j-=1
    return dec

def bin(n):
    bin=""
    while(n!=0):
        bin=str(n%2)+bin
        n=n//2
    return bin
    
def twos(n):
    twos=""
    ones=""
    n=str(n)
    for i in range (len(n)):
        ones+=flip(n[i])
    ones=list(ones)
    twos=list(ones)
    for i in reversed(range(len(n))):
        if ones[i]=="0":
            twos[i]="1"
            break
        else:
            twos[i]="0"
    twos="".join(twos)
    return twos

def adder(a , b):
    
    if len(a)>len(b):
        b = "0"*(len(a)-len(b))+b
    elif len(b)>len(a):
        a = "0"*(len(b)-len(a))+a
    
    result = ""
    carry=0

    for i in range(len(a)-1,-1,-1):
                
        x = int(a[i])
        y = int(b[i])
        Sum = x^y^carry
        carry = (x&y)|((x^y)&carry)
        result =result+(str(Sum))  
        
    return result[::-1], carry
                            
def main(): 
    a = int(input("Enter the first  number: "))
    b = int(input("Enter the second  number: "))
    if a<0 and b<0:
        a = bin(abs(a))
        b = bin(abs(b))

        if len(a)>len(b):
            b = "0"*(len(a)-len(b))+b
        elif len(b)>len(a):
            a = "0"*(len(b)-len(a))+a

        a= "0"+a
        b= "0"+b
        twos_a = twos(a)
        twos_b = twos(b)
        
        
        result ,overflow= adder(twos_a,twos_b)
        print("\nResult is: ",result)
        result = twos(result)
        result = dec(result)
        if overflow == 1: 
            print("Overflow detected\nThe result is negative of ",result)   
        else:
            print("The result is negative of ",result)   
    else:
        a = bin(abs(a))
        b = bin(abs(b))
        
        result , overflow = adder(a,b)
        result = (str(overflow)+str(result))
        new = dec(result)
        if overflow == 1:
            print("\nBinary result: ",result)
            print("Overflow detected\nResult is: ",str(new))
        else:
            print("\nBinary result: ",result)
            print("The result is: ",str(new))
        
if __name__=="__main__":
    main()