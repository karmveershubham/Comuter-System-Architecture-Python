#Write a program to implement bit-wise Subtraction of two numbers using 2’s complement.
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

def flip(n):
    if n=="1":
        return "0"
    else:
        return"1"

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
    print(twos)
    return twos

def adder(num1 , num2):
    num1 = str(int(num1))
    num2 = str(int(num2))
    
    if len(num1)>len(num2):
        num2 = "0"*(len(num1)-len(num2))+num2
    elif len(num2)>len(num1):
        num1 = "0"*(len(num2)-len(num1))+num1
    
    result = ""
    carry=0
    carry2 = None
    for i in range(len(num1)-1,-1,-1):
                
        x = int(num1[i])
        y = int(num2[i])
        Sum = x^y^carry
        carry = (x&y)|((x^y)&carry)
        result =result+(str(Sum))
        if i == 1:
            carry2 = carry
        if carry != carry2:
            return result[::-1] , 1
        else:
            return result[::-1] ,0 
        
    return result[::-1] , carry
                            
def main(): 
    num1 = int(input("enter the first  number"))
    num2 = int(input("enter the second  number"))
    if num1 < 0 and num2<0:
        num1 = abs(num1)
        num2 = abs(num2)
        num1 = bin(num1)
        num2 = bin(num2)
        if len(num1)>len(num2):
            num2 = "0"*(len(num1)-len(num2))+num2
        elif len(num2)>len(num1):
            num1 = "0"*(len(num2)-len(num1))+num1
        num1= "0"+num1
        num2 = "0"+num2
        twos_num1 = twos(num1)
        twos_num2 = twos(num2)
        
        
        result ,overflow= adder(twos_num1,twos_num2)
        print("result is ",result)
        result = twos(result)
        result = bin(result)
        if overflow == 1: 
            print("overflow detected the result is negative of ",result)   
        else:
            print("the result is negative of ",result)   
    else:
        num1 = abs(num1)
        num2 = abs(num2)
        num1 = bin(num1)
        num2 = bin(num2)
        
        result , overflow = adder(num1,num2)
        result = (str(overflow)+str(result))
        new = bin(str(result))
        if overflow == 1:
            print(result)
            print("overflow",str(new))
        else:
            print(result)
            print("the result is ",str(new))
        
if __name__=="__main__":
    main()