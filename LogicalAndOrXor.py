def binary(n): #convert decimal to binary
    bin=""
    while(n!=0):
        bin = str(n%2) + bin
        n = n//2
    
    return bin


def decimal(num): #convert binary to decimal
    dec=0
    j=len(num)-1
    for i in num:
        dec = dec + int(i)*2**j
        j-=1
        
    return dec
        


def binaryLength(a,b): #getting equal length for a and b
    lenA=len(a)
    lenB=len(b)
    
    if(lenA>lenB):
        n=lenA - lenB
        b=n*"0"+b
    elif(lenB>lenA):
        n=lenB - lenA
        a=n*"0"+a

    return [a,b]


def And(a,b):   #calculate logical AND of a and b
    a=binary(a)
    b=binary(b)

    BList = binaryLength(a,b)
    a = BList[0]
    b = BList[1]

    Result=""
    for i in range(len(a)):
        if(a[i]=="0" or b[i] =="0"):
            Result = Result + "0"
        else:
            Result = Result + "1"

    return decimal(Result)



def Or(a,b):   #calculate logical OR of a and b
    a=binary(a)
    b=binary(b)

    BList = binaryLength(a,b)
    a = BList[0]
    b = BList[1]

    Result=""
    for i in range(len(a)):
        if(a[i]=="1" or b[i] =="1"):
            Result = Result + "1"
        else:
            Result = Result + "0"
            
    return decimal(Result)

	

def Xor(a,b):   #calculate logical XOR of a and b
    a=binary(a)
    b=binary(b)

    BList = binaryLength(a,b)
    a = BList[0]
    b = BList[1]


    Result=""
    for i in range(len(a)):
        if(a[i]=="1" and b[i] =="1"):
            Result = Result + "0"
        elif(a[i]=="1" and b[i] =="0") or (a[i]=="0" and b[i] =="1"):
            Result = Result + "1"
        else:
            Result = Result + "0"
            
    return decimal(Result)

def main():
    
    while(True):
        while(True):
            a=int(input("Enter first number  "))
            b=int(input("Enter second number  "))

            if(a<0 or b<0):
                print("Enter Positive number only")
            else:
                break
            
        print("\nTo perform : ")
        print("1. AND Operation between Two number")
        print("2. OR  Operation between Two number")
        print("3. XOR Operation between Two number")

        while(True):
            print("\nEnter a choice.")
            n = int(input())

            if(n==1):
                print(a, " AND ",b," = ", And(a,b))
                print(a, "in binary : ",binary(a))
                print(b, "in binary : ",binary(b))
                print(And(a,b), "in binary : ",binary(And(a,b)))
                break
            elif(n==2):
                print(a, " OR ",b," = ", Or(a,b))
                print(a, "in binary : ",binary(a))
                print(b, "in binary : ",binary(b))
                print(Or(a,b), "in binary : ",binary(Or(a,b)))
                break
            elif(n==3):
                print(a, " XOR ",b," = ", Xor(a,b))
                print(a, "in binary : ",binary(a))
                print(b, "in binary : ",binary(b))
                print(Xor(a,b), "in binary : ",binary(Xor(a,b)))
                break
            else:
                print("WRONG CHOICE ")
                print("Enter Again")
            

        c=input("\nDo you want to continue.: ")
        if(c.lower()!='y'):
            print("THANKS !")
            break
            
        
if __name__=="__main__":
    main()
